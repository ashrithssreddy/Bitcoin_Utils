import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_bitcoin_data(start_date, end_date):
    """Fetch Bitcoin price data between start_date and end_date (limited to the past 365 days)."""
    
    # CoinGecko only allows data within the last 365 days
    max_days_ago = datetime.now() - timedelta(days=365)
    
    # Ensure start_date and end_date are within the allowed range
    if start_date < max_days_ago:
        print("Start date exceeds the 365-day limit. Adjusting start date to the maximum allowed.")
        start_date = max_days_ago
    if end_date > datetime.now():
        print("End date exceeds the current date. Adjusting end date to today.")
        end_date = datetime.now()

    # Ensure start_date is not after end_date
    if start_date > end_date:
        print("Start date is after end date. Please provide a valid date range.")
        return None

    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    params = {
        'vs_currency': 'usd',
        'from': int(start_date.timestamp()),
        'to': int(end_date.timestamp())
    }
    
    response = requests.get(url, params=params)
    
    # Check for errors in the response
    if response.status_code != 200:
        print(f"Error fetching data: {response.json()}")
        return None

    data = response.json()
    
    # Extract prices and convert to DataFrame
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
    
    return prices

# Example usage:
start = datetime(2023, 1, 1)
end = datetime(2023, 9, 1)
bitcoin_prices = fetch_bitcoin_data(start, end)

# If data was successfully fetched, display the first few rows
if bitcoin_prices is not None:
    print(bitcoin_prices.head())
