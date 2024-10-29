
# Key Generation from a 12-Word Seed Phrase

This document explains how a single 12-word seed phrase can generate addresses and private keys for multiple blockchain networks.

---

## 1. Start with a 12-Word Seed Phrase

Suppose your wallet gives you the following 12-word seed phrase:

**Seed Phrase:**  
"ocean gentle claw forest bamboo cradle spoon adapt dizzy arrow jump orphan"

This phrase is the starting point. From this seed phrase, we can generate a master key that will help us derive private keys and addresses for different blockchains.

---

## 2. Generate the Master Key

Using the seed phrase, the wallet software applies a mathematical function to generate the master private key and master chain code. These two together are called the master key pair. This is the "root" key pair, from which all other private keys are derived.

For illustration purposes:

- **Master Private Key:** `xprv9s21ZrQH143K2BWUe8SuS2K8U9YfqpxGZzrc5XgKpqvwjF8rB9SuDnETV1sUzZ3LCxSxnVu46fkpQpeSCu5rsQnyPSF7tKGF9DKUcPgoWZ9`
- **Master Chain Code:** `873dff81c02f525623fd1fe5144ebf9df55d6d56d1d785f2e2be9f3d5b1da52e`

This master key is like a "parent key" and will be used to generate child keys for different blockchains.

---

## 3. Derive Keys and Addresses for Different Blockchains

The wallet uses derivation paths (special formulas) to generate unique private keys and addresses for each network from the master key.

### Example: Deriving Keys for Bitcoin (BTC)

- **Derivation Path for BTC:** `m/44'/0'/0'/0/0`
- **BTC Private Key (derived from master key):**  
  `L1aW4aubDFB7yfras2S1mMEbsS5Djo4wtkFJ73rdDgkX1w79Vho8`
- **BTC Address (generated from BTC private key):**  
  `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`

So, from the seed phrase, we derived a specific private key for Bitcoin, which in turn gave us a Bitcoin address. You can now use this address to send or receive BTC.

---

### Example: Deriving Keys for Ethereum (ETH)

- **Derivation Path for ETH:** `m/44'/60'/0'/0/0`
- **ETH Private Key (derived from master key):**  
  `0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10`
- **ETH Address (generated from ETH private key):**  
  `0x742d35Cc6634C0532925a3b844Bc454e4438f44e`

Similarly, this private key corresponds to an Ethereum address, which is used for ETH and compatible tokens (like USDC, as it’s an ERC-20 token).

---

### Example: Deriving Keys for Base (Layer 2 Network)

Since Base is an Ethereum-compatible network, it uses the same derivation path as Ethereum: `m/44'/60'/0'/0/0`

- **Base Private Key (same as Ethereum private key):**  
  `0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10`
- **Base Address (same as Ethereum address):**  
  `0x742d35Cc6634C0532925a3b844Bc454e4438f44e`

Because Base uses the same address format as Ethereum, the ETH private key can be used directly on the Base network.

---

## Summary Table of Generated Addresses

| Network        | Derivation Path      | Private Key (Derived)                                 | Address                                    |
|----------------|----------------------|------------------------------------------------------|--------------------------------------------|
| Bitcoin        | m/44'/0'/0'/0/0      | L1aW4aubDFB7yfras2S1mMEbsS5Djo4wtkFJ73rdDgkX1w79Vho8 | 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa         |
| Ethereum       | m/44'/60'/0'/0/0     | 0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10 | 0x742d35Cc6634C0532925a3b844Bc454e4438f44e |
| Base           | m/44'/60'/0'/0/0     | 0x4c0883a69102937d6231471b5dbb6204fe51296170827963e29d01c8e99fcd10 | 0x742d35Cc6634C0532925a3b844Bc454e4438f44e |

---

## How Your Wallet Uses This

When you open Coinbase Wallet and switch to Bitcoin, it looks up the BTC address using `m/44'/0'/0'/0/0`. When you switch to Ethereum or Base, it uses `m/44'/60'/0'/0/0` for both. This lets you hold multiple cryptocurrencies in one wallet, securely managed by a single 12-word seed phrase.
