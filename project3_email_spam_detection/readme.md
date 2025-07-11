---
📧 Email Spam Detection App

A simple web app to detect if an email message is spam or not using:

✅ Traditional Machine Learning (Logistic Regression And Naive Bayes + TF-IDF)

✅ Zero-Shot Transformers (BART Model)


Built with Python, Scikit-learn, Hugging Face Transformers, and Streamlit.


---

🚀 Demo Link

👉 Live App["https://email-spam-detectors.streamlit.app/"]


---

📂 Project Structure

project3_email_spam_detection/  
│
├── app.py                  # Streamlit app script  
├── spam_model.pkl         # Saved traditional ML model  
├── tf-idf_vectorizer.pkl  # Saved TF-IDF vectorizer  
├── requirements.txt       # Required Python packages


---

✅ Features

Two Methods to Detect Spam:

Logistic Regression and Naive Bayes + TF-IDF

Zero-Shot Transformers (No fine-tuning needed)


User-friendly Web Interface with Streamlit



---

🛠 Installation

Clone the repository:

git clone https://github.com/Aparna10010/NLP-Transformers_Projects.git
cd NLP-Transformers_Projects/project3_email_spam_detection

Install dependencies:

pip install -r requirements.txt

Run locally:

streamlit run app.py


---

📊 How It Works

Traditional ML:

Email text → TF-IDF Vectorizer → Logistic Regression or Naive Bayes → Spam or Ham


Zero-Shot Transformers:

Email text → BART Large MNLI Model → Spam or Ham based on prompt labels




---

⚙ Requirements

Python 3.8+

scikit-learn

transformers

streamlit

joblib



---

🙋‍♀ Author

Aparna Sharmaa



---

