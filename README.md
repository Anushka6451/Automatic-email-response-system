# 📧 Automatic Email Response System (AI-Powered)

## 🚀 Overview

This project is an **Automatic Email Response System for Citizens** that:

* Reads incoming emails using IMAP
* Classifies them using a **Machine Learning model**
* Generates appropriate responses
* Sends replies automatically using SMTP

It is designed to reduce manual effort in handling large volumes of citizen queries.

---

## 🎯 Features

* 📥 Fetch unread emails automatically
* 🧠 ML-based email classification
* ✉️ Auto-response generation
* 📊 Clean modular architecture
* 💾 SQLite database support
* 🌐 Dashboard (optional UI)

---

## 🧠 Technologies Used

* Python
* IMAP & SMTP (Email handling)
* scikit-learn (ML model)
* pandas (data processing)
* joblib (model saving/loading)
* HTML/CSS (dashboard)

---

## 📁 Project Structure

```
email_auto_response/
│
├── app/
│   ├── main.py
│   ├── email_reader.py
│   ├── email_sender.py
│   ├── database.py
│   ├── response_generator.py
│   ├── scheduler.py
│
├── ML_model/
│   ├── train_model.py
│   ├── predictions.py
│   ├── dataset.csv
│   ├── model.pkl
│   └── __init__.py
│
├── dashboard/
│   └── index.html
│
├── config.py
├── requirements.txt
└── emails.db
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone / Download Project

```
git clone <your-repo-link>
cd email_auto_response
```

---

### 🔹 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 🔹 3. Install Dependencies

```
pip install pandas scikit-learn joblib
pip install beautifulsoup4
```

---

### 🔹 4. Configure Email Credentials

Edit `config.py`:

```python
EMAIL_ACCOUNT = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
IMAP_HOST = "imap.gmail.com"
```

⚠️ Use **App Password**, not your real Gmail password.

---

### 🔹 5. Train the ML Model

Go to ML folder:

```
cd ML_model
python train_model.py
```

✔ This will generate:

```
model.pkl
```

---

### 🔹 6. Run the System

Go back to root folder:

```
cd ..
python -m app.main
```

---

## 🔄 System Workflow

```
Email → Read → Parse → ML Model → Category → Generate Response → Send Email
```

---

## 📊 Categories Supported

* Refund
* Delivery Issue
* Complaint
* Inquiry
* Payment Issue
* Return
* Cancellation
* Feedback
* Technical Issue

---

## 📌 Example

### Input Email:

```
"I want a refund for my order"
```

### Output:

```
Category: refund  
Response: Your refund request has been received...
```

---

## ⚠️ Common Errors & Fixes

### ❌ ModuleNotFoundError

✔ Ensure correct imports and folder names
✔ Run using:

```
python -m app.main
```

---

### ❌ model.pkl not found

✔ Train model first
✔ Fix path using `os.path.join`

---

### ❌ CSV parsing error

✔ Use quotes around text with commas

---

### ❌ SMTP errors

✔ Use App Password
✔ Enable less secure apps (if needed)

---

## 🚀 Future Enhancements

* 🤖 AI-generated dynamic responses
* 📊 Real-time dashboard integration
* 📈 Model accuracy tracking
* ☁️ Cloud deployment
* 🔐 Authentication system

---

## 🏆 Conclusion

This project demonstrates:

* Practical use of **Machine Learning in automation**
* Integration of **email systems with AI**
* Real-world application for **citizen services**

---

## 👩‍💻 Author

Developed as part of an academic project on:
**“Automatic Email Response System for Citizens”**

---

## ⭐ Tip

For best results:

* Use more dataset samples
* Improve model accuracy
* Add dynamic AI responses

---

💡 Your system is now **fully automated + AI-powered** 🚀
