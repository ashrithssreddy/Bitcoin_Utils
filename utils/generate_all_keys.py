from mnemonic import Mnemonic
from bip32utils import BIP32Key
import hashlib
import base58

# Seed phrase
seed_phrase = "oxygen business lecture cream sad write vote fly rate also ozone type"
print("Seed:", seed_phrase, "\n")

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