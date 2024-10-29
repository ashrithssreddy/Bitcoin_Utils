
# Keys: Understanding Private Keys, Public Keys, and QR Codes

## Private Key and Seed Phrase

A **private key** is like a secret password that gives you full control over your Bitcoin. Private keys are generated once during the creation of a wallet, and anyone with access to your private key can spend the Bitcoin associated with it, so keeping it secure is absolutely crucial.

A **seed phrase** (or recovery phrase) is a series of 12-24 words that can be used to regenerate your private key. Think of the seed phrase as the "backup" of your wallet. The seed phrase is a more practical way to memorize or store information compared to the private key, as it is easier to handle. It is also important to note that the direction of generation is one-way: the seed phrase generates the private key, but the private key cannot be used to recreate the seed phrase.

**Not your keys, not your coins**: Anyone who gains access to your private key or seed phrase will have full control over your Bitcoin. This is why it is essential to keep these secure and private.

### Examples
- Private keys are typically long alphanumeric strings like: `5J3mBbAH58CerZLKkss4mBHTaue2c8sF4K6qv2T95sqzSje4xA`.
- A seed phrase might look like: `curve combine shine antique random pistol exhibit coral include syrup ritual figure`.

### Best Practices for Keeping Them Secure
- **Offline Storage**: Write down your seed phrase and store it in a secure, offline place like a safe.
- **Avoid Digital Copies**: Avoid storing your private key or seed phrase in digital form (e.g., on a computer or cloud service).
- **Use a Hardware Wallet**: Hardware wallets offer a secure way to store private keys and are generally resistant to malware.

For more information on keeping your private key secure, check out this [guide on seed phrases](https://bitcoin.org/en/protect-your-privacy).

## Public Keys

A **public key** is mathematically derived from your private key. It’s used to generate your **Bitcoin address**, which is like your account number where others can send Bitcoin to you. Unlike a private key, sharing your public key does not compromise the security of your funds.

Public keys ensure privacy and security, as they are one-way generated from the private key, making it practically impossible to reverse-engineer the private key.

**How Public Keys Are Generated**: When you set up a Bitcoin wallet, it generates a private key, which is then used to derive your public key. Depending on the type of wallet you use and its settings, the public address format might vary to support different Bitcoin address standards, such as:

- **Legacy (P2PKH)**: These addresses start with a “1” (e.g., `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`).
- **P2SH (Pay-to-Script-Hash)**: These start with a “3” and support multisig or other complex scripts (e.g., `3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5`).
- **SegWit (Bech32)**: These start with “bc1” and offer lower fees by using segregated witness (SegWit), which separates transaction signatures from transaction data (e.g., `bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq`).

### Example
- A public key may look like: `03b1d5efb6c8392e9b66cd8545d6c8d01e64c7b94c7b6b14922f31ebff3a2b0e12`.

For more technical details on how public keys are generated, you can refer to this [detailed explanation on elliptic curve cryptography](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm).

### Public Key Types

| **Public Key Type**        | **Description**                                       | **Example Format**     | **Usage**                         | **Wallet Apps Supporting This Type**                    |
|----------------------------|-------------------------------------------------------|-------------------------|-----------------------------------|----------------------------------------------------------|
| **Legacy (P2PKH)**         | Public key used in older Bitcoin addresses.           | `1A1zP1...DivfNa`       | Legacy addresses, still widely recognized. | Electrum, Mycelium, Cash App                             |
| **P2SH (Pay to Script Hash)** | Public key represented in a script form, enabling complex spending conditions like multi-sig. | `3FZbgi...ktZc5`        | Common for multi-sig transactions.        | Ledger, Trezor, Electrum                                  |
| **SegWit (Bech32)**        | Native SegWit key type for **lower transaction fees**. | `bc1qar...5fmdq`        | Used to reduce fees and support SegWit transactions. | Ledger, BlueWallet, Wasabi Wallet                         |
| **Lightning**              | Lightning public key for Layer 2 transactions.         | Format varies           | Used for fast, low-cost transactions.     | Phoenix Wallet, Muun, Wallet of Satoshi                   |
| **Compressed**             | Shortened version of the public key (33 bytes).       | `02b1d5...b0e12`        | Widely used; more efficient.             | Electrum, Ledger, Trezor                                  |
| **Uncompressed**           | Full public key (65 bytes).                           | `04b1d5...4d6e8`        | Less common; used in early days.         | Bitcoin Core, Armory                                      |
| **Multi-Signature**        | Generated for multi-sig wallets requiring multiple keys to authorize a transaction. | Combination of keys | Used for shared wallets or added security. | Electrum, Trezor, Armory                                  |

| **Public Key Type**        | **Description**                                       | **Example Format**                        | **Usage**                         | **Wallet Apps Supporting This Type**                    |
|----------------------------|-------------------------------------------------------|------...------|-----------------------------------|----------------------------------------------------------|

| **Legacy (P2PKH)**         | Public key used in older Bitcoin addresses.           |Addres...ivfNa`| Legacy addresses, still widely recognized. | Electrum, Mycelium, Cash App                             |

| **P2SH (Pay to Script Hash)** | Public key represented in a script form, enabling complex spending conditions like multi-sig. |Addres...ktZc5`| Common for multi-sig transactions. | Ledger, Trezor, Electrum                                  |

| **SegWit (Bech32)**        | Native SegWit key type for **lower transaction fees**. |Addres...f5mdq`| Used to reduce fees and support SegWit transactions. | Ledger, BlueWallet, Wasabi Wallet                         |

| **Lightning**              | Lightning public key for Layer 2 transactions.         |Genera...nnels.| Used for fast, low-cost transactions. | Phoenix Wallet, Muun, Wallet of Satoshi                   |

| **Compressed**             | Shortened version of the public key (33 bytes).       |`02b1d...b0e12`| Widely used; more efficient.      | Electrum, Ledger, Trezor                                  |

| **Uncompressed**           | Full public key (65 bytes).                           |`04b1d...4d6e8`| Less common; used in early days.  | Bitcoin Core, Armory                                      |

| **Multi-Signature**        | Generated for multi-sig wallets requiring multiple keys to authorize a transaction. |Combin...7f...`| Used for shared wallets or added security. | Electrum, Trezor, Armory                                  |


### Cross-Compatibility in Different Wallets
If you load your wallet's private key or seed phrase into another Bitcoin wallet app, it should regenerate your addresses and allow you to receive BTC across all the address types it supports. However, the app's compatibility with different address types depends on its feature set. Most modern wallets support multiple address formats, including Legacy, SegWit, and Bech32, but not all wallets allow you to choose the address type for every transaction.

### Receiving BTC on Different Address Types
You can receive BTC on any valid Bitcoin address format supported by your wallet. The Bitcoin network doesn’t restrict the types of addresses you can use for receiving funds, but transaction fees may vary slightly depending on the address type you use. SegWit (bc1) addresses, for instance, often incur lower fees compared to legacy addresses.

## QR Codes

**QR codes** are commonly used in Bitcoin transactions to easily share wallet addresses. QR codes provide a way for users to scan the Bitcoin address instead of manually typing it, reducing the risk of errors.

### How to Use QR Codes
- **Receiving Bitcoin**: When you want to receive Bitcoin, your wallet app will generate a QR code that contains your Bitcoin address. The sender simply scans it, and the address is automatically entered for them.
- **Sending Bitcoin**: Most wallets allow you to scan the QR code of the recipient to input their address quickly and accurately.

### Example
- Below is an example of what a Bitcoin wallet QR code might look like:
  ![QR Code Example](http://cryptowales.co.uk/wp-content/uploads/2018/08/Private-Keys.png)

### Security Note
- Always **double-check** the address after scanning to ensure it matches the intended recipient, as there are malware programs that attempt to alter addresses.

For more on using QR codes securely in transactions, read this [Bitcoin QR Code Guide](https://bitcoin.org/en/getting-started#payment).

---

These core concepts are critical for understanding how Bitcoin transactions work and how to secure your funds. If you’re interested in more detailed technical material, explore the [Bitcoin Wiki](https://en.bitcoin.it/wiki/Main_Page).