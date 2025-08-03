import feedparser
from textblob import TextBlob
import pandas as pd
from datetime import datetime

def fetch_news(query, max_articles=50):
    feed_url = f"https://news.google.com/rss/search?q={query}+when:30d&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries[:max_articles]:
        published = entry.published if 'published' in entry else datetime.now().isoformat()
        date = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %Z').date()
        title = entry.title
        sentiment = TextBlob(title).sentiment.polarity

        articles.append({
            'date': date,
            'title': title,
            'sentiment': sentiment
        })

    return pd.DataFrame(articles)

if __name__ == "__main__":
    df = fetch_news("Infosys")
    df.to_csv("data/news_data.csv", index=False)
    print(f"✅ Scraped and saved {len(df)} articles to data/news_data.csv")
