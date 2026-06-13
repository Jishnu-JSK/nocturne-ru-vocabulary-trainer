# Nocturne

A minimalist Russian vocabulary explorer built with Flask and powered by a dataset of over **9,000 Russian words**.

Nocturne focuses on simplicity, speed, and an elegant monochrome design inspired by modern productivity applications.

---

## Features

### 📚 Vocabulary Explorer

* Search Russian words instantly
* Search English meanings
* Browse thousands of vocabulary entries
* Clean card-based interface

### 🎯 Practice Mode

* Flashcard-style learning
* Type the English meaning
* Instant answer checking
* Previous / Next navigation
* Random card mode

### ⚡ Lightweight

* No database required
* Excel-powered dataset
* Fast startup
* Simple deployment

---

## Screenshots

### Home

<img width="1436" height="990" alt="Screenshot 2026-06-07 at 10 37 14 PM" src="https://github.com/user-attachments/assets/91842233-a284-466d-8fa4-985b9bba6e05" />


### Vocabulary

<img width="1436" height="988" alt="Screenshot 2026-06-07 at 9 59 46 PM" src="https://github.com/user-attachments/assets/e258dd24-b8be-4e2b-a0ce-0726d803a1e7" />

### Practice

<img width="1436" height="988" alt="Screenshot 2026-06-07 at 10 50 19 PM" src="https://github.com/user-attachments/assets/8685724e-7806-47ab-b4cf-b67e4a300be7" />

---

## Tech Stack

### Backend

* Python
* Flask
* Pandas

### Frontend

* HTML5
* CSS3
* JavaScript

### Dataset

* Excel (.xlsx)
* 9,196 Russian vocabulary entries

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Jishnu-JSK/nocturne-ru-vocabulary-trainer.git

cd nocturne-ru-vocabulary-trainer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
Nocturne/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── russian_words.xlsx
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── vocabulary.html
│   └── practice.html
│
├── static/
│   ├── css/
│   │   └── style.css
├── images/
│   │   └── soviet-bg.jpg
│   │
│   └── js/
│
└── README.md
```

---

## Keyboard Shortcuts

| Key   | Action        |
| ----- | ------------- |
| Enter | Check answer  |
| →     | Next card     |
| ←     | Previous card |

---

## Future Improvements

* Word detail pages
* Favorites system
* Pronunciation audio
* Progress tracking

---

## Author

Jishnu Suresh

GitHub: https://github.com/Jishnu-JSK

