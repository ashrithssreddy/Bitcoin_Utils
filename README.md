# **Bitcoin Utilities (bitcoin_utils)**
This repository serves as a comprehensive suite of data science utilities and tools tailored to the Bitcoin ecosystem. It is designed for developers, quantitative analysts, and crypto enthusiasts who seek advanced solutions for:

### **Overview**
[![Bitcoin](https://img.shields.io/badge/Bitcoin-BTC-yellow.svg?logo=bitcoin)](https://bitcoin.org)
[![Project Status](https://img.shields.io/badge/Project%20Status-In%20Progress-green)](https://github.com/ashrithssreddy/bitcoin_utils)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)](https://github.com/ashrithssreddy/bitcoin_utils)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ashrithssreddy/bitcoin_utils)

- **Bitcoin transaction optimization**
- **Dynamic fee calculation based on mempool data**
- **Seed phrase validation (BIP-39)**
- **Portfolio management with Bitcoin exposure**

### **Key Features**
---

- **Dynamic Bitcoin Transaction Fee Estimator**:
  Leverages mempool data to provide accurate fee estimations, enabling users to optimize transaction costs based on current network conditions. Supports priority-based fee calculations (e.g., low, medium, high priority).

- **BIP-39 Seed Phrase Validator**:
  Implements a manual validation method for BIP-39 seed phrases, ensuring both word validity and checksum accuracy. This goes beyond standard validation, offering transparency into how BIP-39 works under the hood.

- **Private Key Generator**:
  Converts BIP-39 seed phrases into Bitcoin private keys (WIF format) while enforcing strict validation for wordlists and checksum integrity. It supports optional passphrase encryption, adding another layer of security.

- **Live Bitcoin Price Fetcher**:
  Retrieves real-time Bitcoin prices in any supported fiat currency, offering flexibility for multi-currency Bitcoin valuation.

### **Installation**

```bash
git clone https://github.com/ashrithssreddy/bitcoin_utils.git
cd bitcoin_utils
pip install -r requirements.txt
```

### **How to Use**
---

#### 1. **Dynamic Fee Estimation**

This tool calculates dynamic transaction fees based on the current mempool state, allowing for optimal fee selection.

```python
from utils.dynamic_transaction_fee import calculate_dynamic_transaction_fee

transaction_size = 250  # Transaction size in bytes
priority = 'medium'  # Options: 'low', 'medium', 'high'
fee = calculate_dynamic_transaction_fee(transaction_size, priority)
print(f"Estimated Fee: {fee} satoshis")
```

#### 2. **Seed Phrase Validation**

Validate a BIP-39 seed phrase, ensuring it follows the entropy-checksum structure and contains only valid BIP-39 words.

```python
from utils.bip39_validator import validate_bip39_checksum

seed_phrase = "abandon ability able about above absent absorb abstract absurd abuse access accident"
valid = validate_bip39_checksum(seed_phrase)
print(f"Seed Phrase Valid: {valid}")
```

#### 3. **Private Key Generation from Seed Phrase**

Convert a validated seed phrase into a private key (WIF format), with optional passphrase support for enhanced security.

```python
from utils.generate_private_key import generate_private_key_from_seed

seed_phrase = "abandon ability able about above absent absorb abstract absurd abuse access accident"
private_key_wif = generate_private_key_from_seed(seed_phrase)
print(f"Private Key (WIF): {private_key_wif}")
```

### **Contributing**

Contributions are welcome! Feel free to open a pull request or issue to propose new features or improvements.

### **License**

This repository is licensed under the MIT License. See the LICENSE file for details.
