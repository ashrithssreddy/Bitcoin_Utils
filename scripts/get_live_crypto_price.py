import requests

def get_live_crypto_price(crypto_id='bitcoin', vs_currency='usd'):
    """
    Fetch the current live price of a specified cryptocurrency in the specified currency.
    
    Args:
        crypto_id (str): The cryptocurrency ID (e.g., 'bitcoin', 'ethereum').
        vs_currency (str): The currency to compare against (e.g., 'usd', 'eur').
    
    Returns:
        float: The live price of the cryptocurrency in the specified currency.
    """
    
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_id,       # The cryptocurrency ID (e.g., 'bitcoin', 'ethereum')
        'vs_currencies': vs_currency  # The currency to compare against (e.g., 'usd', 'eur')
    }
    
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if crypto_id in data:
            crypto_price = data[crypto_id][vs_currency]
            return crypto_price
        else:
            print(f"Error: Cryptocurrency '{crypto_id}' not found.")
            return None
    else:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return None

# Example usage:
crypto_id = 'bitcoin'  # Change to any supported cryptocurrency (e.g., 'ethereum', 'litecoin')
vs_currency = 'usd'    # Change to any supported fiat currency (e.g., 'eur', 'inr')
live_price = get_live_crypto_price(crypto_id, vs_currency)

if live_price is not None:
    print(f"The current live price of {crypto_id.capitalize()} in {vs_currency.upper()} is: {live_price}")
