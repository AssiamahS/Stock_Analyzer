import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

# Function to scrape healthcare news
def scrape_healthcare_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [headline.text for headline in soup.find_all('h3')]
    return headlines

# Function to fetch stock data
def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, period="1d")
    return stock_data

# Function to generate buy/sell/hold rating
def generate_rating(stock_data):
    if stock_data['Volume'].iloc[-1] > stock_data['Volume'].iloc[-2] and stock_data['Close'].iloc[-1] > stock_data['Close'].iloc[-2]:
        return "Buy"
    elif stock_data['Volume'].iloc[-1] > stock_data['Volume'].iloc[-2] and stock_data['Close'].iloc[-1] < stock_data['Close'].iloc[-2]:
        return "Sell"
    else:
        return "Hold"

# Example usage
url = "https://www.healthline.com/health-news"
ticker = "WW"
headlines = scrape_healthcare_news(url)
stock_data = fetch_stock_data(ticker)
rating = generate_rating(stock_data)

print("Headlines:", headlines)
print("Stock Data:", stock_data)
print("Rating:", rating)
