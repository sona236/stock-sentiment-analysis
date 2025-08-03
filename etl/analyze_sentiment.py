import pandas as pd
import matplotlib.pyplot as plt

# Load the scraped data
df = pd.read_csv("data/news_data.csv")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and calculate average sentiment
daily_sentiment = df.groupby('date')['sentiment'].mean()

# Plot sentiment trend over time
plt.figure(figsize=(10, 5))
daily_sentiment.plot(marker='o')
plt.title("Daily Average Sentiment for Infosys News")
plt.xlabel("Date")
plt.ylabel("Average Sentiment Polarity")
plt.grid(True)
plt.tight_layout()
plt.show()
