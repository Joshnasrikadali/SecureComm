# 🔐 SecureComm

> A Secure Communication System with End-to-End Encrypted File Transfer built using Flask and Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

SecureComm is a secure file communication system that enables users to encrypt and decrypt files using password-based End-to-End Encryption (E2EE).

The system ensures that files remain confidential by encrypting them before storage or transfer. Only users with the correct password can decrypt and access the original content.

The project also provides secure authentication, activity tracking, and a clean, modern dashboard for managing encrypted files.

---

## ✨ Features

- 🔐 Password-based End-to-End Encryption
- 📁 Secure File Upload & Download
- 🔓 File Decryption with Password Verification
- 👤 User Registration & Login
- 🔑 Secure Password Hashing
- 📊 User Activity History
- 👨‍💼 Admin & User Roles
- 🎨 Responsive Modern User Interface
- 🗄 SQLite Database Integration
- ⚡ Fast and Lightweight Flask Backend

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Cryptography
- Werkzeug

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- SQLite

---

## 📂 Project Structure

```
SecureComm/
│
├── app.py
├── config.py
├── crypto.py
├── models.py
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│       ├── login_bg.jpg
│       └── dashboard_bg.jpg
│
├── uploads/
└── README.md
```

---

## 🔒 Security Features

- Password-based file encryption
- PBKDF2 key derivation
- SHA-256 hashing algorithm
- Random salt generation
- Fernet symmetric encryption
- Secure password hashing using Werkzeug
- User session management
- Role-based access control

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/Joshnasrikadali/SecureComm.git
```

Move into the project folder

```bash
cd SecureComm
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 👤 Default Admin Account

```
Username : admin

Password : Admin@123
```

---

## 🚀 How It Works

### User Registration

- Create a new account
- Login securely

### Encrypt File

- Choose a file
- Enter an encryption password
- Download the encrypted `.enc` file

### Decrypt File

- Upload the encrypted file
- Enter the correct password
- Download the original file

---

## 📸 Screenshots

### Login Page

Add screenshot here

```
images/login.png
```

### Dashboard

Add screenshot here

```
images/dashboard.png
```

### Encryption

Add screenshot here

```
images/encryption.png
```

---

## 📦 Dependencies

- Flask
- Flask-SQLAlchemy
- Cryptography
- Werkzeug
- Gunicorn
- psycopg2-binary

---

## 🔮 Future Enhancements

- Two-Factor Authentication (2FA)
- Email Verification
- Secure File Sharing via Link
- Cloud Storage Integration
- AES-256 Encryption Support
- Multi-user Collaboration
- Dark Mode
- File Expiration
- Audit Logs
- Mobile Application

---

## 👩‍💻 Author

**Joshna Sri Kadali**

Bachelor of Computer Science (MSCS)

GitHub:
https://github.com/Joshnasrikadali

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---
