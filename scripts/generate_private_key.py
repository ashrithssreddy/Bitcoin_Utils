from mnemonic import Mnemonic
from bit import Key

def generate_valid_seed_phrase():
    """
    Generate a valid BIP-39 seed phrase.
    
    Returns:
        str: A valid 12-word BIP-39 seed phrase.
    """
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)  # Generates a 12-word seed phrase
    return seed_phrase

def validate_seed_phrase(seed_phrase):
    """
    Validate a BIP-39 seed phrase for correct word count, valid words, and checksum.
    
    Args:
        seed_phrase (str): The BIP-39 seed phrase to validate.
    
    Returns:
        None: If the seed phrase is valid.
    
    Raises:
        ValueError: If the seed phrase is invalid.
    """
    mnemo = Mnemonic("english")
    seed_words = seed_phrase.split()

    # Step 1: Validate word count (must be 12, 15, 18, 21, or 24)
    valid_word_counts = [12, 15, 18, 21, 24]
    if len(seed_words) not in valid_word_counts:
        raise ValueError(f"Invalid word count. Seed phrase must be one of the following word counts: {valid_word_counts}.")
    
    # Step 2: Validate each word in the seed phrase is a valid BIP-39 word
    bip39_wordlist = mnemo.wordlist
    invalid_words = [word for word in seed_words if word not in bip39_wordlist]
    
    if invalid_words:
        raise ValueError(f"Invalid words in seed phrase: {', '.join(invalid_words)}. Ensure all words are valid BIP-39 words.")
    
    # Step 3: Validate the checksum
    if not mnemo.check(seed_phrase):
        raise ValueError("Invalid BIP-39 seed phrase. Checksum does not match.")

def generate_private_key_from_seed(seed_phrase, passphrase=""):
    """
    Generate a private key from a BIP-39 seed phrase after validating the phrase.
    
    Args:
        seed_phrase (str): The BIP-39 seed phrase.
        passphrase (str): Optional passphrase for extra security (default is empty).
    
    Returns:
        str: The Bitcoin private key in WIF format.
    """
    # Validate the seed phrase
    validate_seed_phrase(seed_phrase)
    
    # Convert the mnemonic seed phrase to a seed using PBKDF2 with SHA512
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(seed_phrase, passphrase)
    
    # Use the seed to generate a private key (first 32 bytes of the seed)
    private_key = Key.from_bytes(seed[:32])
    
    # Return the private key in Wallet Import Format (WIF)
    return private_key.to_wif()

# Example usage:
seed_phrase = generate_valid_seed_phrase()
seed_phrase = "oxygen business lecture cream sad write vote fly rate also ozone type"  # Replace with your actual seed phrase
print(f"Generated Valid Seed Phrase: {seed_phrase}")
passphrase = ""  # Optional passphrase (can be left blank)

try:
    private_key_wif = generate_private_key_from_seed(seed_phrase, passphrase)
    print(f"Generated Private Key (WIF): {private_key_wif}")
except ValueError as e:
    print(f"Error: {e}")
