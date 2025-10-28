import os
import joblib
from utils import clean_text

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'models')

# --- Load model and vectorizer ---
model = joblib.load(os.path.join(MODEL_DIR, 'essay_model.pkl'))
vectorizer = joblib.load(os.path.join(MODEL_DIR, 'vectorizer.pkl'))

def predict_score(essay_text):
    """Predict essay score"""
    cleaned = clean_text(essay_text)
    tfidf_text = vectorizer.transform([cleaned])
    score = model.predict(tfidf_text)
    return round(float(score[0]), 2)

# --- Run example ---
if __name__ == "__main__":
    essay = input("Enter your essay: ")
    predicted_score = predict_score(essay)
    print(f"Predicted Score: {predicted_score}")
