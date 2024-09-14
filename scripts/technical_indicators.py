import pandas as pd

def calculate_moving_average(data, window):
    """Calculate moving average."""
    return data['price'].rolling(window=window).mean()

def calculate_rsi(data, window):
    """Calculate RSI (Relative Strength Index)."""
    delta = data['price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Example usage:
bitcoin_data = pd.DataFrame({'price': [30000, 31000, 32000, 33000, 34000]})
ma = calculate_moving_average(bitcoin_data, window=3)
rsi = calculate_rsi(bitcoin_data, window=14)
print(ma)
print(rsi)
