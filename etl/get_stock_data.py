import yfinance as yf
import pandas as pd

ticker = "INFY.NS"  # Infosys on NSE
data = yf.download(ticker, start="2022-01-01", end="2024-12-31")
data.reset_index(inplace=True)
data.to_csv("data/historical_prices.csv", index=False)

print("✅ Stock data saved.")
