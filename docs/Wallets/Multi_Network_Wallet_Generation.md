
# Using a 12-Word Seed Phrase to Generate Multi-Network Wallet Addresses

Let’s go through how a single 12-word seed phrase in your wallet enables it to securely generate addresses and private keys for different networks like Bitcoin, Ethereum, and Base.

---

## 1. Start with a 12-Word Seed Phrase

Suppose your wallet gives you this 12-word seed phrase:

**Seed Phrase:**  
"ocean gentle claw forest bamboo cradle spoon adapt dizzy arrow jump orphan"

This phrase is your wallet’s recovery phrase and the starting point for all key generation. But how does it convert into the keys and addresses for different networks?

---

## 2. Seed Phrase to Master Key Conversion Process

**Process Name:** Key Derivation  
**Function Used:** PBKDF2-HMAC-SHA512  

Here’s what happens:

1. The 12-word seed phrase is converted into a 512-bit binary seed using PBKDF2 (Password-Based Key Derivation Function 2) with the HMAC-SHA512 hashing algorithm.
2. This binary seed, for example, might look like this:

    `5eb00bbddcf069084889a8ab9155568165f5c518b32eb47b2e8a9430e6d7adfd888f8a2e0f95625b24dbdc1997c214b8d306b0834fe3e96d44a2a9ad0bd76098`

3. This 512-bit seed is then used to create the master private key and master chain code, which together form the master key pair.

These keys are the "parent" keys from which all other private keys are derived.

Example of Master Key Pair:

- **Master Private Key:** `xprv9s21ZrQH143K2BWUe8SuS2K8U9YfqpxGZzrc5XgKpqvwjF8rB9SuDnETV1sUzZ3LCxSxnVu46fkpQpeSCu5rsQnyPSF7tKGF9DKUcPgoWZ9`
- **Master Chain Code:** `873dff81c02f525623fd1fe5144ebf9df55d6d56d1d785f2e2be9f3d5b1da52e`

With the master key pair ready, we can now use it to derive specific private keys for each blockchain.

---

## 3. Master Key + Derivation Path to Derived Keys (BTC, ETH, Base)

**Process Name:** Child Key Derivation  
**Function Used:** HMAC-SHA512 as part of the BIP-32 standard  

Using BIP-32, the wallet software applies HMAC-SHA512 to the master private key, master chain code, and a derivation path (a unique identifier for each network) to generate unique child private keys and addresses for each blockchain.

### Example: Deriving Keys for Bitcoin (BTC)

- **Bitcoin Derivation Path:** `m/44'/0'/0'/0/0`
- **BTC Private Key (derived from master key):** `L1aW4aubDFB7yfras2S1mMEbsS5Djo4wtkFJ73rdDgkX1w79Vho8`
- **BTC Address (generated from BTC private key):** `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`

The derivation path and master key together produce a private key for Bitcoin, which in turn generates a Bitcoin address. This address can now be used to send or receive BTC.

### Example: Deriving Keys for Ethereum (ETH)

- **Ethereum Derivation Path:** `m/44'/60'/0'/0/0`
- **ETH Private Key (derived from master key):** `0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10`
- **ETH Address (generated from ETH private key):** `0x742d35Cc6634C0532925a3b844Bc454e4438f44e`

This process produces a unique Ethereum private key and address, which is compatible with Ethereum tokens like ETH, USDC (an ERC-20 token), and more.

### Example: Deriving Keys for Base (Layer 2 Network)

Since Base is compatible with Ethereum, it uses the same derivation path as Ethereum: `m/44'/60'/0'/0/0`

- **Base Private Key (same as Ethereum private key):** `0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10`
- **Base Address (same as Ethereum address):** `0x742d35Cc6634C0532925a3b844Bc454e4438f44e`

Since Base follows Ethereum standards, the ETH address generated is usable on Base as well.

---

## Summary Table of Generated Addresses

| Network        | Derivation Path      | Private Key (Derived)                                 | Address                                    |
|----------------|----------------------|------------------------------------------------------|--------------------------------------------|
| Bitcoin        | m/44'/0'/0'/0/0      | L1aW4aubDFB7yfras2S1mMEbsS5Djo4wtkFJ73rdDgkX1w79Vho8 | 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa         |
| Ethereum       | m/44'/60'/0'/0/0     | 0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10 | 0x742d35Cc6634C0532925a3b844Bc454e4438f44e |
| Base           | m/44'/60'/0'/0/0     | 0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10 | 0x742d35Cc6634C0532925a3b844Bc454e4438f44e |

---

## Step-by-Step Summary of the Process

| Step Description                            | Example Process                                                                                                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **12-word Seed Phrase**                     | `ocean gentle claw forest bamboo cradle spoon adapt dizzy arrow jump orphan`                                                                                             |
| **Seed Phrase to Master Key (Key Derivation)** | PBKDF2-HMAC-SHA512 produces a 512-bit binary seed (e.g., `5eb00bbddcf069084889a8ab9155568165f5c518b32eb47b2e8a9430e6d7adfd888f8a2e0f95625b24dbdc1997c214b8d306b0834fe3e96d44a2a9ad0bd76098`) and generates the master private key and master chain code |
| **Master Key + BTC Derivation Path**        | `m/44'/0'/0'/0/0` generates BTC child private key → BTC address                                                                    |
| **Master Key + ETH Derivation Path**        | `m/44'/60'/0'/0/0` generates ETH child private key → ETH address                                                                    |
| **Master Key + Base Derivation Path**       | `m/44'/60'/0'/0/0` (same as ETH) generates Base child private key → Base address (same as ETH)                                     |
