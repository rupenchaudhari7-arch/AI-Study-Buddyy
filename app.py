from flask import Flask, render_template, request
from summarizer import summarize_text
from quiz_generator import generate_quiz

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    quiz = []

    if request.method == "POST":
        text = request.form.get("input_text")
        summary = summarize_text(text)
        quiz = generate_quiz(summary)

    return render_template("index.html", summary=summary, quiz=quiz)

if __name__ == "__main__":
    app.run(debug=True)
