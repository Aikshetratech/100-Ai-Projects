from textblob import TextBlob
from preprocess import clean_text

def analyze_sentiment(text):
    """
    Returns sentiment polarity: 
    >0 : positive, <0 : negative, 0 : neutral
    """
    cleaned = clean_text(text)
    blob = TextBlob(cleaned)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, polarity
