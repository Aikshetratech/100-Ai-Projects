import re
import string
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords if not already
nltk.download('stopwords', quiet=True)
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """Preprocess essay text: lowercase, remove punctuation/numbers/stopwords"""
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = [word for word in text.split() if word not in STOPWORDS]
    return ' '.join(words)

def preprocess_essays(essay_list):
    """Apply cleaning to a list of essays"""
    return [clean_text(essay) for essay in essay_list]

def evaluate_model(y_true, y_pred):
    """Evaluate model performance"""
    from sklearn.metrics import mean_squared_error, r2_score
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {'mse': mse, 'r2': r2}
