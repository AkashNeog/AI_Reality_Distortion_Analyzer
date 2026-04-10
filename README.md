# 🧠 AI Reality Distortion Analyzer

An AI-powered web application that detects **manipulation, bias, and truthfulness** in textual content such as news, social media posts, and conversations.

---

## 🚀 Live Demo

👉 https://airealitydistortionanalyzer-aey6plfbgtscwezlmjrute.streamlit.app/

---

## 📌 Overview

In today’s digital world, misinformation spreads rapidly through emotionally charged and biased content. This project aims to go beyond traditional sentiment analysis and instead focuses on:

* Identifying **Fact vs Opinion**
* Detecting **emotional influence** (fear, anger, etc.)
* Recognizing **manipulation techniques**
* Generating a **Reality Score (0–100)**
* Providing **human-readable explanations**

---

## ✨ Features

* 🟢 **Fact vs Opinion Classification**
* 🎭 **Emotion Detection (AI-based)**
* ⚠️ **Manipulation Detection** (urgency, fear, bias)
* 📊 **Reality Score System**
* 💡 **Explainable AI Output**
* 🌐 **Interactive Web UI using Streamlit**

---

## 🧠 How It Works

1. User inputs text (news, chat, article)
2. Text is split into sentences
3. Each sentence is analyzed using:

   * NLP models (Transformers)
   * ML classifier (Logistic Regression)
4. System detects:

   * Emotion
   * Fact/Opinion
   * Manipulation patterns
5. A **Reality Score** is calculated
6. Results are displayed with explanations

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI/NLP:** HuggingFace Transformers
* **ML Model:** Scikit-learn (Logistic Regression)

---

## 📂 Project Structure

```
project/
│
├── app.py              # Streamlit UI
├── model.py            # AI + NLP logic
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 🧪 Sample Input

```
If we don’t act now, everything will collapse. This is the only solution and everyone must follow it immediately.
```

---

## 📊 Sample Output

* Type: Opinion
* Emotion: Fear
* Manipulation: Urgency / Pressure
* Reality Score: Low
* Explanation: Uses emotional pressure to influence decision-making

---

## 🎯 Use Cases

* Fake news detection
* Social media content analysis
* Debate & argument analysis
* Educational tool for critical thinking

---

## 🚀 Future Enhancements

* 🔗 Browser extension (real-time detection)
* 📄 PDF / article upload
* 🧠 LLM-based advanced explanations
* 🌍 Multi-language support

---

## 👨‍💻 Author

**Akash Neog**

* B.Tech CSE Student
* AI & Software Development Enthusiast

---

## ⭐ Contributing

Feel free to fork this repo, improve the model, and submit a pull request!

---

## 📜 License

This project is open-source and available under the MIT License.
