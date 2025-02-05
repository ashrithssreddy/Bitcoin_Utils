from hashlib import sha256
from mnemonic import Mnemonic

def get_bip39_wordlist():
    """Retrieve the official BIP-39 wordlist."""
    mnemo = Mnemonic("english")
    return mnemo.wordlist

def validate_bip39_checksum(seed_phrase):
    """
    Validate a BIP-39 seed phrase by manually checking the checksum.
    
    Args:
        seed_phrase (str): The BIP-39 seed phrase to validate.
    
    Returns:
        bool: True if the seed phrase is valid, False otherwise.
    """
    wordlist = mnemo.wordlist # get_bip39_wordlist()
    seed_words = seed_phrase.split()

    # Step 1: Convert the seed phrase words to their corresponding indices in the wordlist
    indices = []
    for word in seed_words:
        if word not in wordlist:
            raise ValueError(f"Invalid word '{word}' found in the seed phrase.")
        indices.append(wordlist.index(word))
    
    # Step 2: Convert the indices to binary and concatenate them into a single binary string
    binary_string = ''.join(f"{index:011b}" for index in indices)  # 11 bits per word
    
    # Step 3: Separate the binary string into entropy and checksum
    entropy_length = (len(seed_words) * 11) - (len(seed_words) // 3)
    entropy_bits = binary_string[:entropy_length]
    checksum_bits = binary_string[entropy_length:]
    
    # Convert the entropy bits back to bytes
    entropy_bytes = int(entropy_bits, 2).to_bytes(len(entropy_bits) // 8, byteorder="big")
    
    # Step 4: Recompute the checksum from the entropy
    hashed_entropy = sha256(entropy_bytes).hexdigest()
    recomputed_checksum_bits = bin(int(hashed_entropy, 16))[2:].zfill(256)[:len(checksum_bits)]
    
    # Step 5: Compare the provided checksum with the recomputed checksum
    return checksum_bits == recomputed_checksum_bits

# Example usage:
seed_phrase = "abandon ability able about above absent absorb abstract absurd abuse access accident"

try:
    is_valid = validate_bip39_checksum(seed_phrase)
    if is_valid:
        print("The seed phrase is valid!")
    else:
        print("Invalid seed phrase: Checksum does not match.")
except ValueError as e:
    print(f"Error: {e}")
