Personalized English Grammar Correction Tool

A web-based intelligent grammar correction app that learns your common writing mistakes over time.
Built using Flask, Transformers, and JSON-based personalization.

🚀 Features

✅ Real-time grammar correction using Transformer models
✅ Personalized learning — adapts to your frequent grammar errors
✅ Clean and modern responsive web interface
✅ Lightweight and easy to deploy locally
✅ JSON-based storage for user-specific corrections

📁 Project Structure
personalized_grammar_tool/
│
├── app.py                    # Flask backend serving API and HTML
├── requirements.txt           # Python dependencies
│
├── data/
│   └── user_mistakes.json    # Stores user-specific grammar mistakes
│
├── src/
│   ├── grammar_corrector.py  # Grammar correction using Transformer model
│   └── personalize.py        # Learns user-specific mistake patterns
│
├── templates/
│   └── index.html            # Main web page UI
│
└── static/
    └── main.js               # Handles frontend API requests

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/personalized_grammar_webapp.git
cd personalized_grammar_webapp

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

🧩 Example requirements.txt
flask
transformers
torch
sentencepiece
nltk

🧠 Run the Application
python app.py


Then open your browser and go to:

http://127.0.0.1:5000

💬 Usage

Type or paste a sentence in the text area.

Click “Correct” to see:

Personalized Sentence (pre-model): text corrected using your previous patterns.

Final Corrected Sentence: model-based perfect grammar output.

The tool automatically learns from each correction and updates user_mistakes.json.

📘 Example

Input:

She go to school everyday.


Personalized Sentence:

She go to school every day.


Corrected Sentence:

She goes to school every day.

🧾 File: data/user_mistakes.json

Example content:

{
  "everyday": "every day",
  "dont": "don't",
  "go": "goes"
}

🪄 Future Improvements

Add user login to save individual mistake profiles

Support for multiple languages

Use a faster lightweight grammar correction model.