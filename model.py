import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def preprocess_text(text):
    sentences = sent_tokenize(text)
    return sentences


emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(sentence):
    result = emotion_model(sentence)[0]
    top_emotion = max(result, key=lambda x: x['score'])
    return top_emotion['label'], round(top_emotion['score'], 2)


texts = [
    "The earth revolves around the sun",
    "I think this movie is amazing",
    "Water boils at 100 degrees",
    "This is the best phone ever",
    "India is in Asia",
    "I believe this policy is wrong",
    "The sky is blue",
    "This is the worst decision ever"
]

labels = ["fact", "opinion", "fact", "opinion", "fact", "opinion", "fact", "opinion"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

fact_model = LogisticRegression()
fact_model.fit(X, labels)

def classify_fact_opinion(sentence):
    vec = vectorizer.transform([sentence])
    return fact_model.predict(vec)[0]


def detect_manipulation(sentence, emotion):
    manipulation_keywords = [
        "act now", "before it's too late",
        "everyone is doing this", "you must",
        "this will destroy", "urgent",
        "no other choice", "guaranteed",
        "shocking truth", "they don't want you to know"
    ]

    sentence_lower = sentence.lower()

    for word in manipulation_keywords:
        if word in sentence_lower:
            return "Urgency / Pressure"

    if emotion in ["fear", "anger"]:
        return "Emotional Manipulation"

    return "None"


def calculate_score(type_label, manipulation, emotion_score):
    score = 100

    if type_label == "opinion":
        score -= 20

    if manipulation != "None":
        score -= 40

    if emotion_score > 0.8:
        score -= 10

    return max(score, 0)


def generate_explanation(type_label, manipulation, emotion):
    if manipulation != "None":
        return f"This sentence uses {manipulation.lower()} and {emotion} emotion to influence the reader."

    elif type_label == "opinion":
        return "This sentence expresses a personal belief rather than a verifiable fact."

    else:
        return "This sentence appears to present factual information."


def analyze_text(text):
    sentences = preprocess_text(text)
    results = []

    for sentence in sentences:
        emotion, emo_score = detect_emotion(sentence)
        fact_op = classify_fact_opinion(sentence)
        manipulation = detect_manipulation(sentence, emotion)
        score = calculate_score(fact_op, manipulation, emo_score)
        explanation = generate_explanation(fact_op, manipulation, emotion)

        results.append({
            "sentence": sentence,
            "type": fact_op,
            "emotion": emotion,
            "emotion_score": emo_score,
            "manipulation": manipulation,
            "score": score,
            "explanation": explanation
        })

    return results
