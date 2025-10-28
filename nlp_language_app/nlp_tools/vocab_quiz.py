import random
from nltk.tokenize import word_tokenize

def load_vocab(file_path):
    """
    Load vocabulary words from a text file.
    Each line: word:meaning
    """
    vocab = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                word, meaning = line.strip().split(":", 1)
                vocab[word.lower()] = meaning
    return vocab

def generate_quiz_from_text(user_text, vocab, n=3):
    """
    Generate a quiz using words from user input and vocab.
    """
    tokens = [w.lower() for w in word_tokenize(user_text) if w.isalpha()]
    selected_words = [w for w in tokens if w in vocab]
    
    # If not enough words, fill with random vocab words
    while len(selected_words) < n:
        word = random.choice(list(vocab.keys()))
        if word not in selected_words:
            selected_words.append(word)
    
    quiz = []
    for word in selected_words[:n]:
        correct = vocab[word]
        choices = [correct]
        # Add 3 random wrong choices
        while len(choices) < 4:
            choice = vocab[random.choice(list(vocab.keys()))]
            if choice not in choices:
                choices.append(choice)
        random.shuffle(choices)
        quiz.append({"word": word, "choices": choices, "answer": correct})
    return quiz
