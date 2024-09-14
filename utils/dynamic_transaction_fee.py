import requests

def get_mempool_fee_estimates():
    """
    Fetch current mempool-based fee estimates for Bitcoin transactions from Blockstream's API.
    
    Returns:
        dict: Fee estimates for different priority levels (in satoshis per byte).
    """
    url = 'https://mempool.space/api/v1/fees/recommended'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching mempool data: {response.status_code}")
        return None

def calculate_dynamic_transaction_fee(transaction_size, priority='medium'):
    """
    Calculate Bitcoin transaction fee dynamically based on current mempool data.
    
    Args:
        transaction_size (int): The size of the transaction in bytes.
        priority (str): The priority level for fee estimation ('low', 'medium', 'high').
    
    Returns:
        int: Estimated transaction fee in satoshis.
    """
    # Fetch mempool fee estimates
    fee_estimates = get_mempool_fee_estimates()
    
    if fee_estimates is None:
        print("Unable to fetch fee estimates.")
        return None
    
    # Map priority to corresponding fee per byte
    fee_per_byte = {
        'low': fee_estimates['hourFee'],      # Fee for confirmation in ~1 hour
        'medium': fee_estimates['halfHourFee'], # Fee for confirmation in ~30 minutes
        'high': fee_estimates['fastestFee']   # Fastest confirmation fee
    }
    
    if priority not in fee_per_byte:
        print(f"Invalid priority level: {priority}. Choose from 'low', 'medium', 'high'.")
        return None
    
    # Calculate the fee based on transaction size and selected priority
    selected_fee_per_byte = fee_per_byte[priority]
    transaction_fee = transaction_size * selected_fee_per_byte
    
    return transaction_fee

# Example usage:
transaction_size = 250  # Transaction size in bytes (standard size)
priority = 'medium'     # Priority level ('low', 'medium', 'high')
estimated_fee = calculate_dynamic_transaction_fee(transaction_size, priority)

if estimated_fee is not None:
    print(f"Estimated transaction fee: {estimated_fee} satoshis (Priority: {priority.capitalize()})")
