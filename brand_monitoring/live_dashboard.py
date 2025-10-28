import streamlit as st
import pandas as pd
from newspaper import Article
from googlesearch import search
import feedparser
from textblob import TextBlob
import plotly.express as px

BRAND = st.sidebar.text_input("Enter Brand Name", "Apple")
NUM_SEARCH_RESULTS = st.sidebar.slider("Google Search Results", 5, 50, 20)
NUM_RSS_RESULTS = st.sidebar.slider("RSS Articles per Feed", 1, 10, 5)
MIN_TEXT_LENGTH = 200

RSS_FEEDS = [
    "https://rss.cnn.com/rss/cnn_topstories.rss",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.theverge.com/rss/index.xml"
]

@st.cache_data(show_spinner=False)
def scrape_news(brand):
    articles = []

    # Google search
    for url in search(f"{brand} news", num_results=NUM_SEARCH_RESULTS):
        try:
            article = Article(url)
            article.download()
            article.parse()
            if len(article.text) < MIN_TEXT_LENGTH:
                continue
            articles.append({"url": url, "title": article.title, "text": article.text})
        except:
            continue

    # RSS feeds
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:NUM_RSS_RESULTS]:
            try:
                url = entry.link
                article = Article(url)
                article.download()
                article.parse()
                if len(article.text) < MIN_TEXT_LENGTH:
                    continue
                articles.append({"url": url, "title": article.title, "text": article.text})
            except:
                continue

    df = pd.DataFrame(articles)
    return df

@st.cache_data(show_spinner=False)
def analyze_sentiment(df):
    if df.empty:
        return df
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
    return df

# --- Streamlit UI ---
st.set_page_config(page_title="Live Brand Monitoring", layout="wide")
st.title("🚀 Live Brand Monitoring Dashboard")

if st.button("Refresh Data"):
    with st.spinner("Scraping articles and analyzing sentiment..."):
        df_articles = scrape_news(BRAND)
        df_articles = analyze_sentiment(df_articles)
        df_articles.to_csv("data/articles_sentiment.csv", index=False)
    st.success("Data refreshed!")

try:
    df_articles
except NameError:
    df_articles = pd.DataFrame()
    try:
        df_articles = pd.read_csv("data/articles_sentiment.csv")
    except:
        pass

if df_articles.empty:
    st.warning("No articles found yet. Click 'Refresh Data' to fetch articles.")
else:
    # Sentiment pie chart
    st.subheader("Sentiment Summary")
    sentiment_counts = df_articles['sentiment'].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']
    fig = px.pie(sentiment_counts, names='Sentiment', values='Count',
                 color='Sentiment', color_discrete_map={'Positive':'green','Neutral':'gray','Negative':'red'})
    st.plotly_chart(fig, use_container_width=True)

    # Recent articles
    st.subheader("Most Recent Articles")
    for idx, row in df_articles.head(10).iterrows():
        st.markdown(f"**[{row['title']}]({row['url']})** - *Sentiment:* {row['sentiment']}")
