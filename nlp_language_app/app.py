from flask import Flask, render_template, request
from nlp_tools import translator, vocab_quiz

app = Flask(__name__)

# Load static vocab
vocab = vocab_quiz.load_vocab("data/sample_vocab.txt")

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    word_info = {}
    quiz = []

    if request.method == "POST":
        text = request.form.get("text", "")
        action = request.form.get("action")
        lang = request.form.get("lang") or "en"

        if action == "translate":
            translation = translator.translate_text(text, lang)
        elif action == "info":
            word_info = translator.get_word_info(text)
        elif action == "quiz":
            quiz = vocab_quiz.generate_quiz_from_text(text, vocab, n=3)

    return render_template("index.html", translation=translation, word_info=word_info, quiz=quiz)

if __name__ == "__main__":
    app.run(debug=True)
