
# Full Derivation Path: `m/44'/0'/0'/0/0`

## Derivation Path Overview

A *derivation path* is a structured way to organize and generate multiple keys and addresses in hierarchical deterministic (HD) wallets. It defines a specific "path" through which addresses are created from a single master seed, allowing users to manage multiple accounts and addresses within one wallet. For example, the derivation path `m/44'/0'/0'/0/0` represents a unique path to a specific Bitcoin address within a user’s wallet.

Each section in the derivation path, separated by slashes (`/`), specifies a different level:

- **m**: the master level (the highest level).
- **44'**: defines the "purpose" or standard to be followed.
- **0'**: specifies the cryptocurrency type.
- **0'**: designates the account number.
- **0/0**: further defines the type (external/internal) and address index.

![BTC Derivation Path](https://thebitcoinmanual.com/wp-content/uploads/2022/08/btc-derivation-path-1.png)

## Master (m)

- **Value:** Always `m`
- **Why it Exists:** Although the value is fixed to `m` for simplicity, it represents the master node of the wallet's HD structure and is always derived from the root seed phrase.
- **The Apostrophe (`'`) Explanation:** The tick mark (`'`) signifies "hardened" derivation, which adds extra security. Hardened paths can only be accessed with the master private key, providing an additional layer of security for critical levels (like purpose, coin type, and account).

## Purpose (`44'`)

- **Typical Values with Examples:**
  - **`44'`:** BIP44 standard for multi-account HD wallets. Example: A standard Bitcoin wallet with addresses starting with “1”, like `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`.
  - **`49'`:** BIP49 for P2SH-wrapped SegWit addresses, commonly starting with "3". Example: A SegWit address such as `3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy`.
  - **`84'`:** BIP84 for Native SegWit (bech32) addresses, commonly starting with "bc1". Example: A Native SegWit address like `bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf7uxh`.
- **Explanation:** The purpose indicates the derivation standard, directing the wallet software to follow specific address formats based on user needs. These standards ensure compatibility across wallets and help users organize their funds based on address types and applications.

## Coin Type (`0'` for Bitcoin)

- **Typical Values:**
  - `0'` - Bitcoin
  - `1'` - Testnet Bitcoin (for testing purposes)
  - `60'` - Ethereum
  - `714'` - Binance Coin
- *(For a complete list of coin types, refer to the [SLIP-0044 registry](https://github.com/satoshilabs/slips/blob/master/slip-0044.md).)*
- **Explanation:** This section tells the wallet which cryptocurrency you’re working with. For instance, `0'` is used for Bitcoin, while `60'` is used for Ethereum.

## Account (`0'`)

- **Typical Values:** Generally starts with `0'` and increases (`0`, `1`, `2`, …) as you create new accounts.
- **Theoretical Limit:** The BIP44 standard theoretically allows up to 2^31 accounts. This vast range means a user could create billions of accounts, but practical limits are set by wallet interfaces.
- **Explanation:** Each account is separate, making it easy to organize funds. For instance, `0'` might be a personal wallet, while `1'` could be a business wallet, ensuring clear fund segregation.

## Change (0 for external, 1 for internal)

- **Typical Values:**
  - `0` - External (used to receive payments from others)
  - `1` - Internal (used to receive “change” from your own transactions)
- **Explanation:**
  - **External Addresses (0):** These are addresses you share with others to receive Bitcoin.
  - **Internal Addresses (1):** When you send Bitcoin, if some is “left over” after the transaction, this “change” is sent back to an internal address within your wallet, so it’s not exposed to the public. This setup keeps your public receiving addresses tidy and reduces the chance of reusing addresses, which is better for privacy.

## Address Index (0)

- **Typical Values:** Starts from `0` and increments (`0`, `1`, `2`, …) as you generate new addresses.
- **Theoretical Limit:** The address index can theoretically go up to 2^31 - 1, allowing a user to create up to 2,147,483,647 unique addresses per account within a derivation path.
- **Explanation:** This is the unique address within a particular derivation path. Each increment in the index generates a new address. You might see `0` for the first address, `1` for the second, and so on, allowing you to create multiple addresses within the same account.
