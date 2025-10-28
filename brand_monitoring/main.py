from src.scrape_news import scrape_news
from src.analyze_sentiment import analyze_sentiment
from src.dashboard import summarize

def main():
    scrape_news()
    analyze_sentiment()
    summarize()

if __name__ == "__main__":
    main()
