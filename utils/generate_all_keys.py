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

    print(f"Child Key {index + 1} Addresses:")
    print(f"  P2PKH Address (Legacy): {p2pkh_address}")
    print(f"  P2SH-P2WPKH Address (Nested SegWit): {p2sh_p2wpkh_address}")
    print(f"  Bech32 Address (Native SegWit): {bech32_address}")
    print()
