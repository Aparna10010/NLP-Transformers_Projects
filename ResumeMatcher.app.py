import streamlit as st
from sentence_transformers import SentenceTransformer, util
import fitz  # PyMuPDF

# Load the sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Function to extract text from PDF or plain text
def upload_resume(source_type="text", value=None):
    if source_type == "pdf":
        docs = fitz.open(stream=value)
        text = ""
        for page in docs:
            text += page.get_text()
        return text

    elif source_type == "text":
        return value
    else:
        raise ValueError("source_type must be 'text' or 'pdf'")


# Upload resume PDF
uploaded_resume = st.file_uploader("Upload your Resume (PDF Only)", type=["pdf"])

# Text area for Job description
job_description = st.text_area("Paste the Job Description here!")

# Buttons
if st.button("Check Similarity"):
    if uploaded_resume and job_description.strip():
        resume_text = upload_resume("pdf", uploaded_resume)

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        job_embedding = model.encode(job_description, convert_to_tensor=True)

        # Calculate Similarity
        similarity_score = util.cos_sim(resume_embedding, job_embedding).item()
        similarity_score = round(similarity_score, 2)

        # Display result
        st.markdown(f'### Similarity Score: **{similarity_score}**')

        # Feedback based on Score
        if similarity_score > 0.85:
            st.success("Excellent Match! Your Resume strongly matches the Job Description.")
        elif similarity_score > 0.65:
            st.info("Good Match! But you might need to add some skills from the Job Description.")
        else:
            st.warning("Poor Match. Revise your resume and include more required skills from the Job Description.")
    else:
        st.error("Please upload a resume in PDF format and paste a Job Description.")
