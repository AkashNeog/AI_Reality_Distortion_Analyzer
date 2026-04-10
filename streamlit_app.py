import streamlit as st
from model import analyze_text

st.set_page_config(page_title="Reality Distortion Detector", layout="wide")

st.markdown(
    """
    <style>
    .stTextArea textarea {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Reality Distortion Detector")
st.write("Analyze text for truth, bias, and manipulation")

user_input = st.text_area("Paste your text here:", height=200)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        results = analyze_text(user_input)

        # Overall Score
        total_score = sum(r["score"] for r in results) // len(results)

        st.subheader(f"📊 Reality Score: {total_score}/100")

        # Score interpretation
        if total_score > 80:
            st.success("Mostly factual content ✅")
        elif total_score > 50:
            st.warning("Mixed content ⚠️")
        else:
            st.error("Highly manipulated / misleading ❌")

        st.markdown("### 🔍 Detailed Analysis")

       
        def get_color(r):
            if r["manipulation"] != "None":
                return "#ff4d4d"  # red
            elif r["type"] == "fact":
                return "#4CAF50"  # green
            else:
                return "#FFA500"  # orange

        
        for r in results:
            color = get_color(r)

            st.markdown(
                f"""
                <div style="
                    padding:15px;
                    margin:10px 0;
                    border-radius:10px;
                    background-color:{color};
                    color:white;">
                    
                    <b>📝 Sentence:</b> {r['sentence']} <br><br>
                    <b>📌 Type:</b> {r['type']} <br>
                    <b>🎭 Emotion:</b> {r['emotion']} ({r['emotion_score']}) <br>
                    <b>⚠️ Manipulation:</b> {r['manipulation']} <br>
                    <b>📊 Score:</b> {r['score']} <br><br>
                    <b>💡 Explanation:</b> {r['explanation']}
                </div>
                """,
                unsafe_allow_html=True
            )
