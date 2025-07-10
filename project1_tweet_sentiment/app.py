import streamlit as st
from transformers import pipeline

# Load the Sentiment - Analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
  result = sentiment_pipeline(text)[0]
  label = result['label']
  score = round(result['score'] * 100,2) # convert to percentage
  return label , score

# Streamlit UI:

st.set_page_config(page_title = "Tweet Sentiment Analyzer", page_icon = "💬")
st.title("💬 Tweet Sentiment Anlaysis App")
st.write("Enter a text or Tweet below to detect its Sentiment")


user_input = st.text_area("Tweet",
                          placeholder = "Type your Tweet here....")
if st.button("Analyze Sentiment"):
  if user_input.strip() == "":
    st.warning("Please enter some text!")
  else:
    label , score = get_sentiment(user_input)
    st.success(f'**Sentiment:** {label}')
    st.info(f'**Confidence:** {score}%')
