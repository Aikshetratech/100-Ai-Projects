import pandas as pd
from textblob import TextBlob

def analyze_sentiment():
    try:
        df = pd.read_csv("data/articles.csv")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("[WARN] No articles to analyze.")
        return

    if df.empty:
        print("[WARN] Articles CSV is empty.")
        return

    sentiments = []
    for text in df['text']:
        polarity = TextBlob(str(text)).sentiment.polarity
        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    df['sentiment'] = sentiments
    df.to_csv("data/articles_sentiment.csv", index=False)
    print("[INFO] Sentiment analysis complete.")
    return df
