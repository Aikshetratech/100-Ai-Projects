Reading Comprehension Quiz Generator (Python)

The Reading Comprehension Quiz Generator is a Python-based project that automatically creates multiple-choice quizzes from reading passages.
It helps learners test their understanding of text passages through interactive, auto-scored quizzes in the terminal.

🚀 Features

✅ Automatically generates quizzes from text passages
✅ Supports multiple passages (auto-load from data/ folder)
✅ Randomized question generation
✅ Interactive command-line interface
✅ Calculates and displays final score
✅ Easy to expand and customize

🗂️ Project Structure
reading_comprehension_quiz/
│
├── data/
│   ├── passage1.txt
│   ├── passage2.txt
│   └── passage3.txt
│
├── src/
│   ├── quiz_generator.py     # Quiz creation logic
│   └── run_quiz.py           # Main script to run the quiz
│
├── requirements.txt          # Dependencies list
└── README.md                 # Project documentation

⚙️ Installation and Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/reading_comprehension_quiz.git
cd reading_comprehension_quiz

2️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run
Run the quiz generator
python src/run_quiz.py


💡 The program will:

Read all .txt files from the data/ folder.

Generate random fill-in-the-blank questions.

Prompt you to answer each question interactively.

Display your final score.

📘 Example Output
--- Passage 1 ---

Q1: Photosynthesis is the process by which green plants convert sunlight into _____ energy.
1. chemical
2. natural
3. physical
4. electrical
Your answer (1-4): 1
✅ Correct!

Q2: The pigment involved in photosynthesis is _____.
1. hemoglobin
2. chlorophyll
3. melanin
4. keratin
Your answer (1-4): 2
✅ Correct!

Score for Passage 1: 2/2
--- Final Score ---
Total: 6/8

🧩 How It Works

quiz_generator.py

Reads the passage text

Randomly selects a sentence

Blanks out one important word

Creates multiple-choice options

run_quiz.py

Loads all passages from the data folder

Displays one quiz per passage

Takes user input and calculates score

🧠 Customization
🔹 Add New Passages

Simply drop new .txt files into the data/ folder:

data/
├── passage1.txt
├── passage2.txt
└── new_passage.txt

🔹 Change Number of Questions

Open src/run_quiz.py and adjust:

quiz = quiz_gen.generate_quiz(num_questions=5)

🧱 Requirements

Python 3.7+

NLTK library

Install manually (if needed):

pip install nltk

🌟 Future Enhancements

Generate short-answer or true/false questions

Integrate with a web interface (Flask/Streamlit)

Use NLP models for smarter question generation

Save quiz results to a file or database