from grammar_corrector import GrammarCorrector
from personalize import Personalizer

def main():
    print("🧠 Personalized English Grammar Correction Tool")
    corrector = GrammarCorrector()
    personalizer = Personalizer()

    while True:
        text = input("\nEnter a sentence (or 'exit' to quit): ").strip()
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Apply personalization
        personalized_text = personalizer.personalize(text)

        # Correct grammar
        corrected = corrector.correct(personalized_text)

        print(f"\n✅ Corrected Sentence: {corrected}")

        # Learn from difference
        personalizer.analyze_and_save(text, corrected)

if __name__ == "__main__":
    main()
