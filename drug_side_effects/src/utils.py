import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['review_text'] = df['review_text'].apply(clean_text)
    return df

def split_data(df, test_size=0.2, random_state=42):
    X = df['review_text']
    y = df['side_effect']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
