import joblib
import streamlit as st
from transformers import pipeline

# Load vectorizer and model
vectorizer = joblib.load("project3_email_spam_detection/tf-idf_vectorizer.pkl")
model = joblib.load("project3_email_spam_detection/spam_model.pkl")

# Load Zero-Shot Classification pipeline
cls = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Streamlit UI
st.title("Email Spam Detection")

# User input
text = st.text_area("Enter Email:")

# Choose model
option = st.selectbox("Choose Method:", ["Traditional ML", "Zero-Shot Transformer"])

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        if option == "Traditional ML":
            features = vectorizer.transform([text])
            result = model.predict(features)[0]
            st.success(f"ML Model Prediction: {result}")
        else:
            labels = ["spam", "ham"]
            result = cls(text, candidate_labels=labels)
            st.success(f"Zero-Shot Prediction: {result['labels'][0]} ({round(result['scores'][0]*100, 2)}% confidence)")
