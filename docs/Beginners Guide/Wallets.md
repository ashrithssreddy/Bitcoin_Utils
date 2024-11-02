
# Wallets

## Wallets - Types
Bitcoin wallets are essential for storing, sending, and receiving Bitcoin securely. Different types of wallets cater to varying needs for security and convenience.

### Hot vs. Cold Wallets
- **Hot Wallets**: Connected to the internet, making them convenient but more susceptible to attacks. Ideal for small, frequent transactions.
  <!-- ![Hot Wallet Example](https://www.investopedia.com/thmb/vsXcdchgpuySmPDAqJb9WUT6Bdc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Hotwallet-vs-Coldwallet-d6d6bb8a8c8445d6bc56888e999a23e6.png) -->
  - Examples: **[Trust Wallet](https://trustwallet.com)**, **[MetaMask](https://metamask.io)** (easy to set up and use, great for small amounts).
- **Cold Wallets**: Offline storage solutions, such as hardware wallets or paper wallets, providing better security for storing larger amounts.
  <!-- ![Cold Wallet Example](https://www.investopedia.com/thmb/vwsf3MxSzrm0xECXcP7eZZ_yF7w=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/cryptocoldstorage-fcd38cd6924748c9b689e86e67417072.png) -->
  - Examples: **Ledger** and **[Trezor](https://trezor.io)** (designed for security, great for long-term storage).


### Restoring Wallets
Restoring a wallet involves using a **seed phrase** (usually 12 or 24 words). This phrase is the master key to your funds, so it's critical to store it securely. 
[How to Restore Your Wallet - Guide](https://cointelegraph.com/learn/how-to-recover-a-crypto-wallet)

### Multi-Sig Wallets - What Are They?
**Multi-signature (multi-sig)** wallets require multiple private keys to authorize transactions. This is particularly useful for:
- Joint accounts, like a shared family wallet.
- Added protection against a single point of failure.  
For example, a wallet might require 2 of 3 signatures to approve a transaction, improving security.

### Custodial vs. Non-Custodial Wallets
- **Custodial Wallets**: A third party (e.g., an exchange) controls your keys. Convenient, but you rely on someone else for security. Think of it as using a bank.
  - Example: **Binance** or **[Coinbase Wallet](https://wallet.coinbase.com)**.
- **Non-Custodial Wallets**: You control your keys, giving you full ownership. It’s akin to keeping cash in your own safe.
  - Example: **Exodus** or **[Electrum](https://electrum.org)** (where only you hold the keys).

## Choosing a Wallet
When choosing a wallet, consider factors like ease of use, security, and the intended purpose of the funds.

### Popular Apps - Examples
- **Hot Wallets**: [Trust Wallet](https://trustwallet.com), [MetaMask](https://metamask.io)
- **Cold Wallets**: Ledger, [Trezor](https://trezor.io)
- **Mobile Wallets**: Cash App, BlueWallet

### Exchange vs. Wallet Difference
- **Exchange Wallet**: Provided by platforms like Binance. You don’t control the keys, and your funds are subject to the exchange’s terms and security.
- **True Wallet**: Lets you hold your own keys, ensuring full ownership and autonomy over your funds.

## Wallet Security Best Practices
Securing your wallet is essential to protecting your Bitcoin. Follow these practices:

- **Hardware Wallets**: Use hardware wallets like Ledger for large amounts.
- **2-Factor Authentication**: Enable 2FA to add an extra layer of security.
- **Backup Strategies**: Keep multiple copies of your seed phrase in secure locations.

## Wallet Security Best Practices

## Paper Wallets - Disposable Ones for Privacy
**Paper wallets** are physical documents that store your private keys. They are suitable for privacy-focused users wanting an offline, disposable wallet.  Examples of websites for creating a paper wallet:
  - **[BitAddress](https://www.bitaddress.org)** - A popular open-source tool for generating Bitcoin paper wallets.
  - **[WalletGenerator](https://www.walletgenerator.net)** - Supports multiple cryptocurrencies for creating paper wallets offline.

## Example Wallet Structure

- **12-Word Seed Phrase** (Example): "cover toast rhythm equip bicycle proud bonus dinner frost spirit pond session"
  - **Master Private Key `xprv9s21ZrQH143K3C5Yx7...` (and Chain Code)**
    - **Spending Wallet** (e.g., Path: m/44'/0'/0')
      - **Everyday Expenses**
        - Path: `m/44'/0'/0'/0/0`
        - Private Key: `L1aW4aubDFB7yfras2S1mEUV...`
        - Public Key: `04a34b...`
        - Bitcoin Address: `1K1Tg1uRcavE7MPxw1SR8qhwqXGsGeQJ5J`
      - **Fun Money for Gadgets**
        - Path: `m/44'/0'/0'/0/1`
        - Private Key: `KzZzRseK3vW1x...`
        - Public Key: `045f7d...`
        - Bitcoin Address: `1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2`
      - **Travel Budget**
        - Path: `m/44'/0'/0'/0/2`
        - Private Key: `L5htzcdKPb4V...`
        - Public Key: `04a3bc...`
        - Bitcoin Address: `1FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5`

    - **Business Wallet** (e.g., Path: m/44'/0'/1')
      - **Client Payments**
        - Path: `m/44'/0'/1'/0/0`
        - Private Key: `L2pCjH4XTKJQ...`
        - Public Key: `048c3d...`
        - Bitcoin Address: `1GdX4fGQ8sD9KZw8UAhTgy4AbdEK3PE9T5`
      - **Vendor Payments**
        - Path: `m/44'/0'/1'/0/1`
        - Private Key: `KwDiBf89QgGbjE...`
        - Public Key: `043b1a...`
        - Bitcoin Address: `1GKFij2meMwrhbzRNp4hJ5tLdy4sbb3R2p`

    - **Savings Wallet** (e.g., Path: m/84'/0'/0') for Native SegWit
      - **2026 Saving for Home Down Payment**
        - Path: `m/84'/0'/0'/0/0`
        - Private Key: `L3vPe6q84A3dGQ...`
        - Public Key: `04d4ae...`
        - Bitcoin Address: `bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwfqdwh`
      - **2031 Car Fund**
        - Path: `m/84'/0'/0'/0/1`
        - Private Key: `KwK3rj3F2dJSh7...`
        - Public Key: `0470e2...`
        - Bitcoin Address: `bc1qq2zk0wjm6dd73h0c6lz4fs0ymf5uxf9xydg5ne`
      - **Emergency Fund**
        - Path: `m/84'/0'/0'/0/2`
        - Private Key: `L4gTs32kPcHz...`
        - Public Key: `04e3ac...`
        - Bitcoin Address: `bc1qpy2vf2zvkv5h3l4h2pn8pjdkl34kjwe8nslme7`

    - **Retirement Wallet** (e.g., Path: m/49'/0'/0')
      - **2050 Retirement Fund**
        - Path: `m/49'/0'/0'/0/0`
        - Private Key: `L5hfds9PRg2e...`
        - Public Key: `046ab1...`
        - Bitcoin Address: `3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy`
      - **Inheritance Fund**
        - Path: `m/49'/0'/0'/0/1`
        - Private Key: `L6G2h8s9FrX2...`
        - Public Key: `0492bd...`
        - Bitcoin Address: `3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC`

    - **Donations Wallet** (e.g., Path: m/44'/0'/2')
      - **Charity Donations**
        - Path: `m/44'/0'/2'/0/0`
        - Private Key: `K1kRf3tG4j7f...`
        - Public Key: `04c3f1...`
        - Bitcoin Address: `1FcbB6Nw23L8Gd6aGr5AbK8BBDsN7BBRaS`
      - **Community Fund**
        - Path: `m/44'/0'/2'/0/1`
        - Private Key: `K9g2Rf8uJ6h9...`
        - Public Key: `04c8f3...`
        - Bitcoin Address: `1Eo4uJfW8th5z7BD2X9ZcHSTQ5H3d7KyM`
