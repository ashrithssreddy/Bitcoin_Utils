from bip44 import Wallet
import requests

def get_balance_from_seed(seed_phrase, network='bitcoin'):
    """
    Derives addresses from a BIP44 seed phrase and calculates the total balance by querying UTXOs.

    Args:
        seed_phrase (str): The BIP39 seed phrase.
        network (str): Blockchain network (default: 'bitcoin').

    Returns:
        float: Total balance in BTC.
    """
    # Initialize a BIP44 wallet from the seed phrase
    wallet = Wallet(seed_phrase)

    # Define the derivation path components (m/44'/0'/0'/0/i for Bitcoin mainnet)
    account = 0  # Default account
    change = False  # Use receiving addresses (not change addresses)

    balance = 0  # Initialize total balance in satoshis

    # Loop through the first 10 addresses (adjust as needed)
    for i in range(10):
        # Generate address for the derivation path m/44'/0'/0'/0/i
        address = wallet.get_address(account=account, change=change, address_index=i, network=network)
        print(f"Checking balance for address: {address}")

        # Fetch UTXOs from Blockstream API
        try:
            response = requests.get(f'https://blockstream.info/api/address/{address}/utxo')
            response.raise_for_status()  # Raise an error for bad responses
            utxos = response.json()

            # Sum up all UTXO values for the address
            for utxo in utxos:
                balance += utxo['value']  # Value is in satoshis
        except requests.RequestException as e:
            print(f"Failed to fetch balance for address {address}: {e}")
            continue

    # Convert balance from satoshis to BTC
    balance_btc = balance / 1e8
    return balance_btc

# Usage
seed_phrase = "disorder piece fetch inflict rib liquid mistake betray skill beauty wheel resource"
try:
    total_balance = get_balance_from_seed(seed_phrase)
    print(f"Total Balance (BTC): {total_balance}")
except Exception as e:
    print(f"Error: {e}")
