# app.py
from flask import Flask, render_template, request
from summarizer import MultilingualSummarizer

app = Flask(__name__)
summarizer = MultilingualSummarizer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    text = request.form['text']
    language = request.form['language']
    summary = summarizer.summarize(text, lang_code=language)
    return render_template('index.html', original_text=text, summary=summary, selected_language=language)

if __name__ == '__main__':
    app.run(debug=True)
