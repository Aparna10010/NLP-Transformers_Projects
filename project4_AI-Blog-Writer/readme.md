
---

# 📝 AI Blog Writer using GPT-2 and BART

An AI-powered blog writing assistant that generates **titles**, **summaries**, and **full blog content** from any topic or paragraph input. Built using Hugging Face’s Transformers and Gradio for an interactive UI.

---

## 🚀 Live Demo

🔗 **Try it here**: [Gradio App](https://d6d46721103b06cf2f.gradio.live/)

---

## 📌 Overview

This app uses transformer models to generate complete blog content:

* 🧠 **GPT-2** for generating blog titles and long-form blog content
* 📰 **facebook/bart-large-cnn** for generating concise summaries

Includes a **user-friendly Gradio interface** for real-time interaction.

---

## ✨ Features

✅ Title Generator using **GPT-2**
✅ Blog Content Generator using **GPT-2**
✅ Summary Generator using **facebook/bart-large-cnn**
✅ Parameter tuning: token limits, temperature, sampling
✅ Clean and simple Gradio UI

---

## 📸 Gradio UI (Screenshot)

> 📷 Add your UI screenshot here:

![Gradio UI Screenshot](https://github.com/Aparna10010/NLP-Transformers_Projects/blob/main/project4_AI-Blog-Writer/Gradio%20Interface.png)

---

## 🛠 Tech Stack

* Python
* Hugging Face Transformers
* PyTorch
* Gradio

---

## 🧪 Models Used

| Task             | Model                     |
| ---------------- | ------------------------- |
| Title Generation | `gpt2`                    |
| Blog Generation  | `gpt2`                    |
| Summarization    | `facebook/bart-large-cnn` |

---

## 📁 Folder Structure

```
AI_Blog_Writer_Project/
├── ai_blog_writer.py          # Gradio app
├── requirements.txt           # Dependencies
├── readme.md                  # Documentation
└── assets/
    └── demo_screenshot.png    # UI Screenshot
```

---

## 🧠 How to Run

```bash
pip install -r requirements.txt
python ai_blog_writer.py
```

---

## 🔄 Future Enhancements

* [ ] Fine-tune GPT-2 and BART on domain-specific blog data
* [ ] Add export options to `.docx` or `.pdf`
* [ ] Integrate Grammarly or plagiarism checker
* [ ] Add tone-based generation (e.g., formal, casual, humorous)

---

## 👩‍💻 Author

**Aparna Sharmaa**
*Data Science Enthusiast | NLP Learner*
[GitHub](https://github.com/Aparna10010) • [LinkedIn](https://www.linkedin.com/in/apsh?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

---

## 📄 License

This project is licensed under the **MIT License**.

---


