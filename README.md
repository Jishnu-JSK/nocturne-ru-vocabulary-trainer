# 🇷🇺 Nocturne

### A minimalist Russian vocabulary explorer built with Flask.

Nocturne is a modern web application designed for learners who want a fast, distraction-free way to explore and practice Russian vocabulary.

Built around a curated dataset of over **9,000 common Russian words**, Nocturne combines powerful search capabilities with a clean monochrome interface inspired by modern productivity tools.

---

## ✨ Features

### 📚 Vocabulary Explorer

Browse and search through thousands of Russian words instantly.

* Russian → English lookup
* English → Russian lookup
* Fast search
* Large vocabulary dataset
* Clean card-based interface

### 🎯 Practice Mode

Improve retention through active recall.

* Randomized vocabulary practice
* Instant answer reveal
* Unlimited practice sessions

### ⚡ Lightweight & Fast

No database required.

Vocabulary is loaded directly from an Excel dataset using Pandas, making setup simple and deployment lightweight.

---

## 🖤 Design Philosophy

Nocturne follows a minimalist design approach inspired by modern applications such as Notion, Linear, and Raycast.

### Principles

* Monochrome color palette
* Minimal distractions
* Typography-first design
* Fast navigation
* Focus on learning

---

## 🛠 Tech Stack

### Backend

* Python
* Flask
* Pandas

### Frontend

* HTML5
* CSS3
* JavaScript

### Data

* Excel (.xlsx)
* 9,000+ Russian vocabulary entries

---

## 📂 Project Structure

```text
nocturne/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── 10000_russian_words.xlsx
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── vocabulary.html
│   ├── word.html
│   ├── practice.html
│   └── 404.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── app.js
│   │
│   └── img/
│
├── screenshots/
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Jishnu-JSK/nocturne.git
cd nocturne
```

### Create Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Dataset

Place the vocabulary dataset inside:

```text
data/10000_russian_words.xlsx
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📈 Roadmap

### Version 1.0

* Vocabulary search
* Practice mode
* Responsive design

### Version 2.0

* Word detail pages
* Favorites system
* Daily word

### Version 3.0

* Pronunciation support
* Flashcards
* Vocabulary collections

### Version 4.0

* Progress tracking
* Learning statistics
* User accounts

---

## 📸 Screenshots

Add screenshots here after deployment.

```text
screenshots/
├── home.png
├── vocabulary.png
└── practice.png
```

---

## 👨‍💻 Author

**Jishnu Suresh**

GitHub: https://github.com/Jishnu-JSK

---

## 📜 License

This project is licensed under the MIT License.

---

### ⭐ Support

If you find Nocturne useful, consider starring the repository.

It helps the project grow and motivates future development.
