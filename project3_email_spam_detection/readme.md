
# 📧 Email Spam Detection App

A complete web application to detect whether an email message is spam or not. This project combines:

- ✅ Traditional Machine Learning (Logistic Regression + Naive Bayes + TF-IDF)
- ✅ Zero-Shot Transformers (BART Model)

Both approaches are integrated into a single Streamlit app for a smooth user experience.

---

## 🎯 Project Highlights

- *Two Detection Methods*:  
  → ML Model: Trained on a labeled dataset using TF-IDF + Logistic Regression or Naive Bayes.  
  → Zero-Shot Learning: Uses BART-large-mnli from Hugging Face Transformers to predict spam or ham without custom training.

- *User-Friendly Interface*:  
  Simple web interface using Streamlit to input text, select a model, and view prediction results instantly.

- *Deployable Anywhere*:  
  Tested with Streamlit Cloud and local deployment.

---

## 📂 Project Structure

- project3_email_spam_detection/ │
├── app.py                 
- Streamlit app script 
├── requirements.txt       
- Python dependencies
├── spam_model.pkl        
- Pre-trained ML model (pickle file)
├── tf-idf_vectorizer.pkl  
- TF-IDF vectorizer (pickle file)
└── README.md              
- Project documentation

---

## 🛠 Tech Stack Used

- *Python 3.9+*
- *Scikit-learn*
- *Hugging Face Transformers*
- *Streamlit*
- *Joblib*

---

## 🚀 Live Demo

👉 [Click Here to Try the App](https://email-spam-detectors.streamlit.app/)

---

## ⚙ Setup & Installation

1. *Clone the repository:*

   ```bash
   git clone https://github.com/Aparna10010/NLP-Transformers_Projects.git
   cd project3_email_spam_detection

2. Install the required packages:

pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run app.py


4. Usage:

Enter the email text in the input box.

Select either:

Traditional Machine Learning

Zero-Shot Transformers


Click "Predict" to get the result.





---

✨ Author

Aparna Sharma




---

💡 Notes

Ensure all .pkl model files are present in the same directory as app.py.

Zero-Shot model may take longer to predict as it loads from Hugging Face Hub.

This project is for learning purposes and may require further optimization for production use.



---

✅ License

This project is open-source and free to use for educational purposes.

