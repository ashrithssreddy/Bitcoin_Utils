# Bitcoin Public Key Verification

## Elliptic Curve Cryptography (ECC) and secp256k1

Bitcoin uses **Elliptic Curve Cryptography (ECC)**, specifically the **secp256k1** curve. This curve is defined by the following equation:

\[
y^2 = x^3 + 7 \ (\text{mod} \ p)
\]

Where:
- \( p = 2^{256} - 2^{32} - 977 \), a prime number defining the finite field.
- \( x \) and \( y \) are coordinates representing points on the elliptic curve.

Public keys in Bitcoin are points on this elliptic curve. To ensure the validity of a public key, it must satisfy this equation, meaning it must correspond to a valid point on the secp256k1 curve.

### Why It Matters

In Bitcoin, public keys are derived from private keys using this elliptic curve, making it computationally infeasible to reverse the process and discover the private key from the public key. This one-way function ensures security in the Bitcoin network.

A valid Bitcoin public key must:
- Be a valid point on the secp256k1 curve.
- Not be the "point at infinity."

### Resources for Further Learning
- [Elliptic Curve Cryptography on Wikipedia](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography): General overview of elliptic curve cryptography.
- [Secp256k1 on LearnMeABitcoin](https://learnmeabitcoin.com/technical/secp256k1)&#8203;:contentReference[oaicite:0]{index=0}: Detailed explanation of the secp256k1 curve used by Bitcoin.
- [2Coins Bitcoin Utility Tools](https://www.2coins.org/)&#8203;:contentReference[oaicite:1]{index=1}: Online tools for converting and verifying Bitcoin public keys.
- [Bitstart Bitcoin Public Key Verification Tool](http://www.bitstart.me/btc-tools/tool/address-to-pubkey)&#8203;:contentReference[oaicite:2]{index=2}: Convert and verify Bitcoin public keys online.
- [Bitcoin.com Tools for Verification](https://www.bitcoin.com/tools/verify-message/)&#8203;:contentReference[oaicite:3]{index=3}: Tool for verifying Bitcoin signed messages.
