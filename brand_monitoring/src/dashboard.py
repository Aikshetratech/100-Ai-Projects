import pandas as pd

def summarize():
    try:
        df = pd.read_csv("data/articles_sentiment.csv")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("[WARN] No sentiment data to summarize.")
        return

    if df.empty:
        print("[WARN] Articles sentiment CSV is empty.")
        return

    summary = df['sentiment'].value_counts()
    print("\n===== Brand Sentiment Summary =====")
    print(summary)
    print("\nMost recent articles:")
    print(df[['title','url','sentiment']].head(5))
