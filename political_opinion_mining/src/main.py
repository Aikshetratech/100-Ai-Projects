import pandas as pd
from sentiment_analysis import analyze_sentiment

# Load dataset
data = pd.read_csv("data/election_tweets.csv")

# Analyze sentiment
results = []
for idx, row in data.iterrows():
    sentiment, polarity = analyze_sentiment(row['text'])
    results.append({
        "id": row['id'],
        "text": row['text'],
        "sentiment": sentiment,
        "polarity": polarity
    })

# Convert to DataFrame
results_df = pd.DataFrame(results)

# Save results
results_df.to_csv("data/election_sentiment_results.csv", index=False)

# Summary
summary = results_df['sentiment'].value_counts()
print("Sentiment Summary:")
print(summary)
