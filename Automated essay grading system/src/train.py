import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

from utils import preprocess_essays, evaluate_model

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'essays.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
os.makedirs(MODEL_DIR, exist_ok=True)

# --- Load and preprocess data ---
data = pd.read_csv(DATA_PATH)
print(f"Loaded {len(data)} essays.")

X = preprocess_essays(data['essay'])
y = data['score']

# --- Feature extraction ---
vectorizer = TfidfVectorizer(max_features=500)
X_tfidf = vectorizer.fit_transform(X)

# --- Train/Test split ---
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# --- Train model ---
model = LinearRegression()
model.fit(X_train, y_train)

# --- Evaluate model ---
y_pred = model.predict(X_test)
metrics = evaluate_model(y_test, y_pred)
print(f"Model Evaluation: MSE={metrics['mse']:.2f}, R2={metrics['r2']:.2f}")

# --- Save model and vectorizer ---
joblib.dump(model, os.path.join(MODEL_DIR, 'essay_model.pkl'))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, 'vectorizer.pkl'))
print(f"Model and vectorizer saved in {MODEL_DIR}")
