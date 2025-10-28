import os
import sys
from quiz_generator import QuizGenerator

# Ensure src folder is in the path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

def load_passages(data_folder):
    passages = []
    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    passages.append(text)
    return passages

def main():
    data_folder = os.path.join(current_dir, "..", "data")
    passages = load_passages(data_folder)

    if not passages:
        print("No passages found in the data folder!")
        return

    total_score = 0
    total_questions = 0

    for p_idx, passage in enumerate(passages, 1):
        print(f"\n--- Passage {p_idx} ---\n")
        quiz_gen = QuizGenerator(passage)
        quiz = quiz_gen.generate_quiz(num_questions=3)

        score = 0
        for idx, q in enumerate(quiz, 1):
            print(f"\nQ{idx}: {q['question']}")
            for i, opt in enumerate(q['options'], 1):
                print(f"{i}. {opt}")
            answer = input("Your answer (1-4): ")
            try:
                if q['options'][int(answer)-1] == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer: {q['answer']}")
            except:
                print(f"Invalid input. Correct answer: {q['answer']}")
        
        print(f"\nScore for Passage {p_idx}: {score}/{len(quiz)}")
        total_score += score
        total_questions += len(quiz)

    print(f"\n--- Final Score ---")
    print(f"Total: {total_score}/{total_questions}")

if __name__ == "__main__":
    main()
