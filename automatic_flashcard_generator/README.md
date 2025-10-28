Automatic Flashcard Generator from Notes

This project automatically generates flashcards (question–answer pairs) from your text notes using Natural Language Processing (NLP).
It helps students and learners quickly revise large amounts of information by turning notes into smart flashcards.

📁 Project Structure
automatic_flashcard_generator/
│
├── data/
│   └── notes.txt                 # Input notes text
│
├── flashcards/
│   └── flashcards.txt            # Generated flashcards (output)
│
├── src/
│   └── flashcard_generator.py    # Main Python script
│
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation

⚙️ Installation & Setup

Clone or download this project folder.

git clone https://github.com/yourusername/automatic_flashcard_generator.git
cd automatic_flashcard_generator


Install required dependencies

pip install -r requirements.txt


Check required files

Put your notes in: data/notes.txt

Example:

Photosynthesis is the process by which green plants convert sunlight into energy. 
It occurs in chloroplasts that contain chlorophyll.

🚀 How to Run

Move to the source directory:

cd src


Run the flashcard generator:

python flashcard_generator.py


Output will be saved at:

../flashcards/flashcards.txt

🧩 Example

Input (data/notes.txt):

The heart pumps blood throughout the body. 
It is made up of four chambers. 
Exercise improves cardiovascular health because it strengthens the heart and lungs.


Output (flashcards/flashcards.txt):

Flashcard 1:
Q: What do you know about The?
A: The heart pumps blood throughout the body.

Flashcard 2:
Q: What is it?
A: made up of four chambers.

Flashcard 3:
Q: Why Exercise improves cardiovascular health?
A: Because it strengthens the heart and lungs.

🧠 Features

✅ Automatically detects definitions, causes, and key facts
✅ Generates flashcards even if “is” / “are” are missing
✅ Uses NLP to summarize long notes (optional)
✅ Works fully offline after model download
✅ Clean and simple structure — easy to extend

⚙️ Dependencies

Listed in requirements.txt:

transformers
torch
nltk


You can install them with:

pip install -r requirements.txt

🧩 How It Works

Reads notes from data/notes.txt

Summarizes text if it’s long (using BART model)

Splits into sentences with NLTK

Generates questions from detected patterns
(“is”, “are”, “because”, “used for”, etc.)

Saves all Q&A pairs into flashcards/flashcards.txt