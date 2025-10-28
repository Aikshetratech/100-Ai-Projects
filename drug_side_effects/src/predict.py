import pickle
from utils import clean_text

# Load trained model
with open('models/side_effect_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Drug Side Effect Predictor")
print("Type 'exit' to quit\n")

while True:
    review = input("Enter a drug review: ")
    if review.lower() == "exit":
        print("Exiting...")
        break
    review_cleaned = [clean_text(review)]
    prediction = model.predict(review_cleaned)
    print(f"Predicted side effect: {prediction[0]}\n")
