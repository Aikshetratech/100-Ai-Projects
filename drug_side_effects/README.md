Drug Side Effect Prediction from Reviews

This project predicts possible side effects mentioned in drug reviews using Natural Language Processing (NLP) and Machine Learning (Naive Bayes classifier).
It processes user-written reviews, trains a text classification model, and predicts the most likely side effect for new inputs.

📁 Folder Structure
drug_side_effects/
│
├── data/
│   ├── raw/
│   │   └── reviews.csv           # Original data (raw input)
│   ├── processed/
│   │   └── processed_data.csv    # Cleaned data for training
│
├── src/
│   ├── utils.py                  # Helper functions (text cleaning, splitting)
│   ├── data_prep.py              # Preprocess and clean text data
│   ├── train.py                  # Train the model
│   ├── predict.py                # Predict side effects from new reviews
│
├── models/
│   └── side_effect_model.pkl     # Trained model file
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation

⚙️ Requirements

Python 3.8+

pip (Python package manager)

Install dependencies (no environment needed):

pip install -r requirements.txt


or manually:

pip install pandas scikit-learn

🧹 Step 1: Prepare Data

Place your drug reviews in:

data/raw/reviews.csv


Example format:

review_text,side_effect
I felt dizzy and tired after taking this tablet,dizziness
The cream caused a rash on my arms,rash


Or you can directly use the provided processed_data.csv (50 sample reviews).

To preprocess and clean the text:

python src\data_prep.py


This creates:

data/processed/processed_data.csv

🤖 Step 2: Train the Model

Train the Naive Bayes model:

python src\train.py


Reads the processed dataset

Splits into train/test sets

Trains a text classifier

Saves the model to: models/side_effect_model.pkl

Example output:

Model Accuracy: 0.89
Model saved to models/side_effect_model.pkl

🔮 Step 3: Predict Side Effects

Run interactive prediction mode:

python src\predict.py


Example session:

Drug Side Effect Predictor
Type 'exit' to quit

Enter a drug review: I had a rash after using this cream
Predicted side effect: rash

Enter a drug review: Felt dizzy and nauseous after the pill
Predicted side effect: dizziness

🧩 Example Outputs
Review Text	Predicted Side Effect
I felt dizzy and nauseous after the pill	dizziness
I had a rash on my arms	rash
My stomach hurt badly after taking it	stomach_pain
I felt very sleepy all day	drowsiness
🚀 Run All Steps at Once

You can create a simple batch file (run_all.bat) in your project folder:

@echo off
python src\data_prep.py
python src\train.py
python src\predict.py
pause


Then just double-click run_all.bat to process, train, and predict automatically.

🧰 Technologies Used

Python

scikit-learn (Machine Learning)

pandas (Data Processing)

TF-IDF Vectorizer (Feature Extraction)

Naive Bayes Classifier

💡 Future Improvements

Use BERT / Transformers for higher accuracy

Add Flask / Streamlit Web Interface

Include multi-label prediction for multiple side effects per review

Visualize common side effects using Plotly or Matplotlib