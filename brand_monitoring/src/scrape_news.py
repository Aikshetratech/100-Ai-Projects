import feedparser
from newspaper import Article
import pandas as pd
from googlesearch import search

BRAND = "Apple"        # Replace with your brand
NUM_SEARCH_RESULTS = 20
NUM_RSS_RESULTS = 5    # Number of articles per RSS feed
MIN_TEXT_LENGTH = 200  # Skip short articles

def scrape_news():
    articles = []

    print("[INFO] Searching Google for articles...")
    for url in search(f"{BRAND} news", num_results=NUM_SEARCH_RESULTS):
        try:
            article = Article(url)
            article.download()
            article.parse()
            if len(article.text) < MIN_TEXT_LENGTH:
                continue
            articles.append({
                "url": url,
                "title": article.title,
                "text": article.text
            })
        except Exception as e:
            print(f"[WARN] Google search article skipped: {e}")
            continue

    print("[INFO] Fetching RSS feeds...")
    rss_feeds = [
        "https://rss.cnn.com/rss/cnn_topstories.rss",
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://www.theverge.com/rss/index.xml"
    ]
    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:NUM_RSS_RESULTS]:
            try:
                url = entry.link
                article = Article(url)
                article.download()
                article.parse()
                if len(article.text) < MIN_TEXT_LENGTH:
                    continue
                articles.append({
                    "url": url,
                    "title": article.title,
                    "text": article.text
                })
            except Exception as e:
                print(f"[WARN] RSS feed article skipped: {e}")
                continue

    if not articles:
        print("[WARN] No articles found for this brand.")
        return pd.DataFrame()

    df = pd.DataFrame(articles)
    df.to_csv("data/articles.csv", index=False)
    print(f"[INFO] Scraped {len(df)} articles.")
    return df

if __name__ == "__main__":
    scrape_news()
