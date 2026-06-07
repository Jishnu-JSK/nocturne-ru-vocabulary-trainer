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

![Home](screenshots/home.png)

### Vocabulary

![Vocabulary](screenshots/vocabulary.png)

### Practice

![Practice](screenshots/practice.png)

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
* Daily word
* Pronunciation audio
* Progress tracking
* Spaced repetition

---

## Author

Jishnu Suresh

GitHub: https://github.com/Jishnu-JSK

---

## License

MIT License
