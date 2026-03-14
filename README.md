# Flask Login & Registration System

A simple **user authentication web application** built using **Flask, MySQL, Flask-WTF, and bcrypt**.
The system allows users to register, securely log in, access a personal dashboard, and log out.

This project demonstrates fundamental concepts of **Python web development**, including authentication, password security, session management, and database integration.

---

## 🚀 Features

* User Registration
* Secure Login Authentication
* Password Hashing using **bcrypt**
* Email Validation with **WTForms**
* Session Management
* User Dashboard
* Logout Functionality
* Form Validation using **Flask-WTF**

---

## 🛠 Technologies Used

* **Python**
* **Flask**
* **Flask-WTF**
* **WTForms**
* **MySQL**
* **bcrypt**
* **HTML**

---

## 📂 Project Structure

```
flask-login-system
│
├── app.py
├── README.md
├── .gitignore
│
└── templates
    ├── index.html
    ├── register.html
    ├── login.html
    └── dashboard.html
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/flask-login-system.git
```

### 2️⃣ Navigate to the project folder

```
cd flask-login-system
```

### 3️⃣ Install dependencies

```
pip install flask
pip install flask-wtf
pip install wtforms
pip install flask-mysqldb
pip install bcrypt
pip install email-validator
```

---

## 🗄 Database Setup

Create a MySQL database and table.

```
CREATE DATABASE DB18;

USE DB18;

CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(255)
);
```

---

## ▶️ Run the Application

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📚 Learning Outcomes

* Understanding the **Flask web framework**
* Implementing **authentication systems**
* Secure password storage with **bcrypt**
* Handling forms with **Flask-WTF**
* Connecting **Flask with MySQL**
* Managing **user sessions**

---

## 📌 Future Improvements

* Password confirmation during registration
* Email verification
* Profile management
* Password reset functionality
* UI improvements using Bootstrap

---


---

⭐ If you found this project useful, consider giving it a star on GitHub!
