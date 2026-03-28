# 📧 AI-Powered Automatic Email Response System with Real-Time Dashboard

---

## 🚀 Project Overview

This project is an **AI-based Automatic Email Response System** designed for handling citizen queries efficiently.

It:

* 📥 Reads incoming emails using IMAP
* 🧠 Classifies emails using a Machine Learning model
* ✉️ Sends automated responses via SMTP
* 💾 Stores email data in a database
* 📊 Displays insights in a **real-time dashboard**

---

## 🎯 Key Features

* 🤖 ML-based email classification
* 📬 Automated email responses
* ⚡ Real-time dashboard (auto-updating)
* 🔍 Search & filtering in dashboard
* 🔔 Live notifications (new email alert)
* 🌙 Dark mode UI
* 🗄️ SQLite database integration

---

## 🧠 Technologies Used

* Python
* Flask (API backend)
* scikit-learn (Machine Learning)
* pandas (data handling)
* joblib (model serialization)
* IMAP & SMTP (email protocols)
* HTML, CSS, JavaScript (dashboard UI)
* Chart.js (data visualization)

---

## 📁 Project Structure

```
email_auto_response/
│
├── app/
│   ├── main.py
│   ├── api.py
│   ├── email_reader.py
│   ├── email_sender.py
│   ├── database.py
│
├── model/
│   ├── train_model.py
│   ├── predict.py
│   ├── dataset.csv
│   ├── model.pkl
│
├── dashboard/
│   └── index.html
│
├── config.py
├── requirements.txt
├── emails.db
└── README.md
```

---

## ⚙️ Environment Setup

### 🔹 1. Install Python

* Recommended: **Python 3.10 – 3.12**
* Minimum: Python 3.8+

---

### 🔹 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 🔹 3. Install Dependencies

Create `requirements.txt`:

```
flask
pandas
scikit-learn
joblib
beautifulsoup4
```

Install:

```
pip install -r requirements.txt
```

---

## 📧 Email Configuration (IMPORTANT)

Edit `config.py`:

```
EMAIL_ACCOUNT = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
IMAP_HOST = "imap.gmail.com"
```

---

### ⚠️ Gmail Setup

You MUST:

1. Enable **2-Step Verification**
2. Generate **App Password**
3. Use App Password instead of normal password

---

## 🧠 Train Machine Learning Model

```
cd model
python train_model.py
```

This will generate:

```
model.pkl
```

---

## 🗄️ Database

* Uses **SQLite (built-in)**
* File auto-created:

```
emails.db
```

---

## 🚀 Running the System

---

### ▶️ Step 1: Start Email Processor

```
python -m app.main
```

---

### ▶️ Step 2: Start Dashboard API

```
python app/api.py
```

---

### ▶️ Step 3: Open Dashboard

```
dashboard/index.html
```

---

## 🔄 System Workflow

```
Email → Read → Parse → ML Model → Category → Save → Respond → Dashboard Update
```

---

## 📊 Dashboard Features

* 📈 Category distribution charts
* 📊 Email statistics (total, processed)
* 🧾 Recent emails table
* 🔍 Search functionality
* 🔔 Live notifications
* 🌙 Dark mode

---

## 📌 Example

**Input Email:**

```
"I want a refund for my order"
```

**System Output:**

```
Category: refund
Response: Your refund request has been received...
```

---

## ⚠️ Common Errors & Fixes

### ❌ ModuleNotFoundError

```
pip install <package>
```

---

### ❌ model.pkl not found

```
python train_model.py
```

---

### ❌ Gmail authentication failed

* Use App Password
* Enable IMAP

---

### ❌ Dashboard not updating

* Ensure Flask API running:

```
http://127.0.0.1:5000/stats
```

---

### ❌ Auto-reply loop issue

Add filter in `main.py`:

```
if any(x in from_.lower() for x in ["postmaster", "noreply", "no-reply"]):
    continue
```

---

## 🏆 Why This Project is Placement-Ready

* Full-stack architecture
* Real-time dashboard
* ML integration
* Clean modular code
* Practical real-world use case

---

## 💼 How to Explain in Interview

```
This system automates email handling using machine learning.
It classifies incoming emails into categories and sends responses automatically.
A real-time dashboard built using Flask and JavaScript provides analytics
and monitoring of email activity.
```

---

## 🚀 Future Enhancements

* 🤖 GPT-based dynamic responses
* 🔐 Authentication system
* ☁️ Cloud deployment (AWS / Render)
* 📈 Model accuracy tracking
* 📊 Advanced analytics

---

## 👩‍💻 Author

**Automatic Email Response System for Citizens**
Anushka 

---

## ⭐ Tip

To improve performance:

* Add more training data
* Tune ML model
* Improve UI/UX

---

💡 Your system is now **AI-powered + real-time + industry-ready** 🚀
