#### Setup ####
from mnemonic import Mnemonic
from bip32utils import BIP32Key
import hashlib
import base58
import qrcode
%config NotebookNotary.db_file = ':memory:' # prevents saving logs and checkpoints locally 
%autosave 0  # Turns off autosave

#### Seed phrase ####
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
    
    # If all checks pass, print a success message
    print("Seed phrase is valid.")

seed_phrase = generate_valid_seed_phrase()
# seed_phrase = "oxygen business lecture cream sad write vote fly rate also ozone type"
passphrase = ""  # Optional passphrase (can be left blank)
print("Seed:", seed_phrase, "\n")
validate_seed_phrase(seed_phrase)

#### Binary Seed
# Initialize the Mnemonic object
mnemo = Mnemonic("english")
print("Mnemonic Object:", mnemo, "\n")  # Printing the mnemonic object

# Generate the binary seed from the seed phrase
binary_seed = mnemo.to_seed(seed_phrase)
print("Binary Seed:", binary_seed, "\n") # hexadecimal format for readability
print("Binary Seed (hex):", binary_seed.hex(), "\n") # hexadecimal format for readability

#### Master Private Key and Master Chain Code
master_key = BIP32Key.fromEntropy(binary_seed)
print("Master Private Key (WIF):", master_key.WalletImportFormat(), "\n")
print("Master Chain Code (hex):", master_key.ChainCode().hex(), "\n")

#### Extended Private Key (xPrv)
print("Extended Private Key (xPrv):", master_key.ExtendedKey(private=True), "\n")

#### Child Private/Public Keys
# Generate and store Child Private and Public Keys for the first few indices
num_children = 5  # Adjust this number to generate more child keys
child_keys = {}
for i in range(num_children):
    child_key = master_key.ChildKey(i)
    child_keys[i] = {
        "private_key": child_key.WalletImportFormat(),
        "public_key": child_key.PublicKey().hex()
    }

# Print the collected child keys
for index, keys in child_keys.items():
    print(f"Child Key {index + 1} (Private): {keys['private_key']}")
    qrcode.make(keys['private_key']).show()
    print(f"Child Key {index + 1} (Public): {keys['public_key']}")

#### Public Addresses
def hash160(data):
    """RIPEMD-160(SHA-256(data))"""
    sha256 = hashlib.sha256(data).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256)
    return ripemd160.digest()

def checksum(data):
    """Calculate the checksum for a given data."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]

def public_key_to_p2pkh_address(public_key):
    """Generate a P2PKH (legacy) address from a public key."""
    prefix = b'\x00'  # Mainnet prefix for P2PKH addresses
    pubkey_hash = hash160(public_key)
    address = prefix + pubkey_hash
    return base58.b58encode(address + checksum(address)).decode()

def public_key_to_p2sh_p2wpkh_address(public_key):
    """Generate a P2SH-P2WPKH (nested SegWit) address from a public key."""
    prefix = b'\x05'  # Mainnet prefix for P2SH addresses
    witness_program = b'\x00\x14' + hash160(public_key)
    address = prefix + hash160(witness_program)
    return base58.b58encode(address + checksum(address)).decode()

def public_key_to_bech32_address(public_key):
    """Generate a Bech32 (native SegWit) address from a public key."""
    import bech32
    witness_program = hash160(public_key)
    return bech32.encode("bc", 0, witness_program)

# Generate and Print Addresses for Each Child Public Key
print("\nGenerated Bitcoin Addresses:\n")
for index, keys in child_keys.items():
    public_key_bytes = bytes.fromhex(keys['public_key'])
    p2pkh_address = public_key_to_p2pkh_address(public_key_bytes)
    p2sh_p2wpkh_address = public_key_to_p2sh_p2wpkh_address(public_key_bytes)
    bech32_address = public_key_to_bech32_address(public_key_bytes)
    qrcode.make(bech32_address).show()

    print(f"Child Key {index + 1} Addresses:")
    print(f"  P2PKH Address (Legacy): {p2pkh_address}")
    print(f"  P2SH-P2WPKH Address (Nested SegWit): {p2sh_p2wpkh_address}")
    print(f"  Bech32 Address (Native SegWit): {bech32_address}")
    print()
