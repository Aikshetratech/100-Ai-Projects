Automated Essay Grading System

An Automated Essay Grading (AEG) system built using Python and Natural Language Processing (NLP).
This tool evaluates essays based on grammar, length, and vocabulary richness, and provides a score out of 10.

📁 Project Structure
automated_essay_grading/
│
├── data/
│   ├── essays.csv              # (Optional) Sample dataset
│
├── src/
│   ├── essay_dataset.py        # (Optional) Dataset loader for ML models
│   ├── grade_model.py          # Core essay grading logic
│   ├── main.py                 # CLI-based interface to grade essays
│
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation

⚙️ Features

✅ Checks grammar quality using TextBlob
✅ Calculates essay length and vocabulary richness
✅ Produces a final score out of 10
✅ Simple command-line interface for testing
✅ Easy to extend with ML/NLP models (like BERT)

🧩 Installation

Clone the repository

git clone https://github.com/yourusername/automated_essay_grading.git
cd automated_essay_grading


Install dependencies

pip install -r requirements.txt


Download TextBlob corpora (only once)

python -m textblob.download_corpora

🧠 Usage

Run the main script:

python src/main.py


Type or paste your essay when prompted:

Automated Essay Grading System
-------------------------------
Enter essay (or type 'exit' to quit):
> This essay demonstrates good structure and grammar overall.


Output:

Predicted Score: 8/10

🧮 Scoring Criteria
Category	Description	Max Points
Grammar Accuracy	Fewer spelling and grammar errors	3
Essay Length	Based on number of words (more is better)	4
Vocabulary Richness	More unique words = higher score	3
Total		10
📊 Example
Essay Input	Predicted Score
“The essay was written clearly and without grammatical errors.”	9/10
“This essay bad grammar and no structure.”	4/10
“Good content but lacks vocabulary diversity.”	6/10
🧱 Future Improvements

Integrate BERT or RoBERTa for semantic scoring

Add coherence, clarity, and content relevance analysis

Web-based interface for uploading essays

Visualization dashboard for performance trends