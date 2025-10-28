import random
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')

class QuizGenerator:
    def __init__(self, passage):
        self.passage = passage
        self.sentences = sent_tokenize(passage)
    
    def generate_question(self):
        # Pick a random sentence
        sentence = random.choice(self.sentences)
        words = word_tokenize(sentence)
        # Pick a random word to mask (not punctuation)
        words_to_choose = [w for w in words if w.isalpha()]
        if not words_to_choose:
            return None
        answer = random.choice(words_to_choose)
        question = sentence.replace(answer, "_____")
        # Generate options
        options = [answer]
        for _ in range(3):
            fake_word = random.choice(words_to_choose)
            while fake_word in options:
                fake_word = random.choice(words_to_choose)
            options.append(fake_word)
        random.shuffle(options)
        return {
            "question": question,
            "answer": answer,
            "options": options
        }

    def generate_quiz(self, num_questions=3):
        quiz = []
        for _ in range(num_questions):
            q = self.generate_question()
            if q:
                quiz.append(q)
        return quiz
