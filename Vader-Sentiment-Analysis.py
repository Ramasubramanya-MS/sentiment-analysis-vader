import streamlit as st
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Initialize VADER SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Streamlit App
st.title("Sentiment Analysis using VADER")
st.markdown("Analyze short reviews and classify them as **Positive**, **Negative**, or **Neutral**")

# Sample input box
st.subheader("Enter Reviews (one per line):")
reviews_input = st.text_area("Paste 10–15 short reviews below:", height=200)

# Analyze Button
if st.button("Analyze Sentiment") and reviews_input.strip():
    reviews = [review.strip() for review in reviews_input.split('\n') if review.strip()]
    results = []

    for review in reviews:
        score = sia.polarity_scores(review)['compound']
        if score > 0.05:
            sentiment = "Positive"
        elif score < -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        results.append({
            "Review": review,
            "Compound Score": round(score, 3),
            "Final Sentiment": sentiment
        })

    # Display as table
    st.subheader("Sentiment Results:")
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

else:
    st.info("Please paste some reviews and click **Analyze Sentiment**.")

