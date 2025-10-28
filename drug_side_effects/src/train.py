import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import load_data, split_data

# Load and split data
df = load_data('data/processed/processed_data.csv')
X_train, X_test, y_train, y_test = split_data(df)

# Build pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', MultinomialNB())
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
accuracy = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
with open('models/side_effect_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)
print("Model saved to models/side_effect_model.pkl")
