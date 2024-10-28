from mnemonic import Mnemonic
from bip32utils import BIP32Key

# Step 1: Seed phrase input
seed_phrase = input("Enter your seed phrase: ")

# Step 2: Generate seed from seed phrase
mnemo = Mnemonic("english")
seed = mnemo.to_seed(seed_phrase)

# Step 3: Generate master private key and extended private key (xPrv)
master_key = BIP32Key.fromEntropy(seed)

# Display the master private key in WIF format
master_private_key_wif = master_key.WalletImportFormat()
print("Master Private Key (WIF):", master_private_key_wif)

# Display the extended private key (xPrv)
print("Extended Private Key (xPrv):", master_key.ExtendedKey(private=True))

# Step 4: Generate and display 10 public keys
print("\nDerived Public Keys:")
for i in range(10):
    derived_key = master_key.ChildKey(i)
    public_key = derived_key.PublicKey().hex()
    print(f"Public Key {i + 1}: {public_key}")
