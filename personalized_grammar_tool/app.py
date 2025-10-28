from flask import Flask, request, jsonify, render_template
from src.grammar_corrector import GrammarCorrector
from src.personalize import Personalizer

app = Flask(__name__)

# Instantiate once (model load may take time)
corrector = GrammarCorrector()
personalizer = Personalizer()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/correct', methods=['POST'])
def api_correct():
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Apply personalization layer
    personalized = personalizer.personalize(text)

    # Model correction (may be slow)
    corrected = corrector.correct(personalized)

    # Save learned pairs from original -> corrected
    personalizer.analyze_and_save(text, corrected)

    return jsonify({
        'original': text,
        'personalized': personalized,
        'corrected': corrected
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
