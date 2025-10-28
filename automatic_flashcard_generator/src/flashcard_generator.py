import os
import nltk
from transformers import pipeline
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Download resources
nltk.download('punkt')
nltk.download('stopwords')

# Paths
NOTES_PATH = "../data/notes.txt"
OUTPUT_PATH = "../flashcards/flashcards.txt"

def read_notes(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def maybe_summarize(text, threshold=150, max_length=80):
    if len(text) < threshold:
        print("📝 Text is short — skipping summarization.")
        return text
    else:
        print("🧠 Summarizing long text...")
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
        return summary[0]['summary_text']

def generate_flashcards(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))
    flashcards = []

    for sent in sentences:
        words = word_tokenize(sent)
        words_clean = [w for w in words if w.isalnum() and w.lower() not in stop_words]

        # Try definition style
        if " is " in sent:
            parts = sent.split(" is ", 1)
            q = f"What is {parts[0].strip()}?"
            a = parts[1].strip()
            flashcards.append((q, a))
        elif " are " in sent:
            parts = sent.split(" are ", 1)
            q = f"What are {parts[0].strip()}?"
            a = parts[1].strip()
            flashcards.append((q, a))
        # Try cause/effect
        elif " because " in sent:
            parts = sent.split(" because ", 1)
            q = f"Why {parts[0].strip()}?"
            a = f"Because {parts[1].strip()}."
            flashcards.append((q, a))
        # Try about "used for" or "used to"
        elif " used for " in sent:
            parts = sent.split(" used for ", 1)
            q = f"What is {parts[0].strip()} used for?"
            a = parts[1].strip()
            flashcards.append((q, a))
        elif " used to " in sent:
            parts = sent.split(" used to ", 1)
            q = f"What is {parts[0].strip()} used to do?"
            a = parts[1].strip()
            flashcards.append((q, a))
        # Try general fact style (fallback)
        elif len(words_clean) > 4:
            keyword = words_clean[0].capitalize()
            q = f"What do you know about {keyword}?"
            a = sent.strip()
            flashcards.append((q, a))

    return flashcards

def save_flashcards(flashcards, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        if not flashcards:
            f.write("⚠️ No flashcards generated. Try longer or more descriptive notes.\n")
            print("⚠️ No flashcards generated. Try longer or more descriptive notes.")
            return
        for i, (q, a) in enumerate(flashcards, 1):
            f.write(f"Flashcard {i}:\nQ: {q}\nA: {a}\n\n")
    print(f"✅ Flashcards saved to {output_path}")

if __name__ == "__main__":
    print("📘 Reading notes...")
    notes = read_notes(NOTES_PATH)

    print("🔍 Checking text length...")
    summary_or_text = maybe_summarize(notes)

    print("💡 Generating flashcards...")
    flashcards = generate_flashcards(summary_or_text)

    print("💾 Saving flashcards...")
    save_flashcards(flashcards, OUTPUT_PATH)

    print("🎉 Flashcard generation complete!")
