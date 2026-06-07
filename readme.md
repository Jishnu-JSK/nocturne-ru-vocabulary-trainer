# Russian Vocabulary Trainer

A modern web-based application designed to help learners build and retain Russian vocabulary through interactive quizzes, progress tracking, streaks, and achievement systems.

## 📖 Overview

Russian Vocabulary Trainer is an educational web application built with Flask and SQLite that allows users to create personalized vocabulary lists and practice them using quiz-based learning techniques.

The project aims to make language learning engaging by incorporating gamification features such as achievements, streak tracking, and performance analytics.

---

## ✨ Features

### 📚 Vocabulary Management

* Add new Russian words and translations
* Edit existing vocabulary entries
* Delete unwanted words
* Organize vocabulary efficiently

### 🎯 Practice Mode

* Randomized vocabulary quizzes
* Instant answer validation
* Score tracking
* Learning progress monitoring

### 📊 Statistics Dashboard

* Total words learned
* Quiz accuracy percentage
* Correct and incorrect answer counts
* Learning history

### 🏆 Achievement System

Unlock achievements as you learn:

| Achievement        | Requirement               |
| ------------------ | ------------------------- |
| First Step         | Add your first word       |
| Vocabulary Builder | Add 50 words              |
| Russian Explorer   | Add 100 words             |
| Quiz Master        | Score 100 correct answers |
| Consistency King   | Maintain a 7-day streak   |
| Language Legend    | Maintain a 30-day streak  |

### 🔥 Streak Tracking

* Daily learning streaks
* Motivation system
* Progress reminders

---

## 🛠️ Tech Stack

### Backend

* Python 3.11+
* Flask
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite

---

## 📂 Project Structure

```text
russian-vocabulary-trainer/
│
├── app.py
├── requirements.txt
├── database.db
│
├── templates/
│   ├── index.html
│   ├── add_word.html
│   ├── practice.html
│   ├── vocab.html
│   ├── stats.html
│   └── achievements.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── screenshots/
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/russian-vocabulary-trainer.git
cd russian-vocabulary-trainer
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Dashboard

Add a screenshot of the dashboard here.

### Practice Mode

Add a screenshot of the quiz interface here.

### Statistics

Add a screenshot of the analytics page here.

---

## 🎓 Educational Benefits

This project helps users:

* Learn Russian vocabulary efficiently
* Improve long-term retention
* Build consistent study habits
* Monitor learning progress
* Stay motivated through gamification

---

## 📈 Future Roadmap

### Version 2.0

* Spaced repetition algorithm
* Vocabulary categories
* Word difficulty levels
* Audio pronunciation support

### Version 3.0

* User authentication
* Cloud synchronization
* PostgreSQL support
* Leaderboards

### Version 4.0

* AI-generated example sentences
* Grammar exercises
* Mobile application
* Offline mode

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 🐛 Reporting Issues

If you encounter a bug or have a feature request:

1. Open an Issue
2. Describe the problem clearly
3. Include reproduction steps
4. Attach screenshots if applicable


---

## 👨‍💻 Author

Developed by **Jishnu Suresh**

GitHub: https://github.com/Jishnu-JSK

---

### ⭐ Support

If you find this project useful, consider giving it a star on GitHub.

Every star helps support future development and improvements.
