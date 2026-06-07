from flask import Flask, render_template, request, redirect, make_response
import pandas as pd
import random
from datetime import date

app = Flask(__name__)

EXCEL_FILE = "data/russian_words.xlsx"

try:
    df = pd.read_excel(EXCEL_FILE)
    df.columns = [str(c).strip() for c in df.columns]
    russian_col = df.columns[0]
    english_col = df.columns[1]
except Exception:
    df = pd.DataFrame(columns=["Russian", "English"])
    russian_col = "Russian"
    english_col = "English"


def get_word_of_the_day():
    if len(df) == 0:
        return {"russian": "", "english": "", "index": 0}
    # Fresh date read every call — changes at midnight, consistent within a day
    today_seed = int(date.today().strftime("%Y%m%d"))
    rng = random.Random(today_seed)
    idx = rng.randint(0, len(df) - 1)
    word = df.iloc[idx]
    return {
        "russian": str(word[russian_col]),
        "english": str(word[english_col]),
        "index": int(idx),
        "today": date.today().isoformat(),
    }


@app.route("/")
def home():
    wotd = get_word_of_the_day()
    resp = make_response(render_template(
        "home.html",
        total=len(df),
        wotd_russian=wotd["russian"],
        wotd_english=wotd["english"],
        wotd_index=wotd["index"],
        today=wotd["today"],
    ))
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/vocabulary")
def vocabulary():
    q = request.args.get("q", "").lower()
    if q:
        filtered = df[
            df[russian_col].astype(str).str.lower().str.contains(q, na=False)
            | df[english_col].astype(str).str.lower().str.contains(q, na=False)
        ]
    else:
        filtered = df.head(100)

    return render_template(
        "vocabulary.html",
        words=filtered.to_dict("records"),
        russian_col=russian_col,
        english_col=english_col,
        query=q,
    )


@app.route("/practice")
def practice_redirect():
    return redirect("/practice/0")


@app.route("/practice/random")
def random_practice():
    if len(df) == 0:
        return redirect("/")
    random_index = random.randint(0, len(df) - 1)
    return redirect(f"/practice/{random_index}")


@app.route("/practice/<int:index>")
def practice(index):
    if len(df) == 0:
        return render_template("practice.html", word=None)

    words = df.to_dict("records")
    total = len(words)
    if index < 0:
        index = 0
    if index >= total:
        index = total - 1

    word = words[index]
    return render_template(
        "practice.html",
        word=word,
        index=index,
        total=total,
        russian_col=russian_col,
        english_col=english_col,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
