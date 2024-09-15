# How a Seed Phrase is Validated Before Generating Private Keys

### Valid Seed Phrase Example:

Let’s use the seed phrase:

`"abandon ability able about above absent absorb abstract absurd abuse access accident"`

### Step-by-Step Validation Process:

1. **Convert Seed Words to Indices**: Each word in the BIP-39 wordlist corresponds to an index (0 to 2047). We look up the indices for each word in the seed phrase:
    * `abandon`: index 0
    * `ability`: index 1
    * `able`: index 2
    * `about`: index 3
    * `above`: index 4
    * `absent`: index 5
    * `absorb`: index 6
    * `abstract`: index 7
    * `absurd`: index 8
    * `abuse`: index 9
    * `access`: index 10
    * `accident`: index 11

   **Resulting Indices**:
   `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

2. **Convert Indices to Binary**: Each index is converted to an 11-bit binary string (since BIP-39 uses 11 bits per word):
    * `abandon`: `00000000000`
    * `ability`: `00000000001`
    * `able`: `00000000010`
    * `about`: `00000000011`
    * `above`: `00000000100`
    * `absent`: `00000000101`
    * `absorb`: `00000000110`
    * `abstract`: `00000000111`
    * `absurd`: `00000001000`
    * `abuse`: `00000001001`
    * `access`: `00000001010`
    * `accident`: `00000001011`

   **Concatenated Binary String**:
   `000000000000000000001000000000110000000010000000001010000000001100000000011100000000100000000010000000001010000000001011`

3. **Split the Binary Data into Entropy and Checksum**: For a 12-word seed phrase, the first 128 bits represent the entropy, and the last 4 bits represent the checksum.

   **Entropy Bits** (first 128 bits):
   `00000000000000000000100000000011000000001000000000101000000000110000000001110000000010000000001000000000101000000000`

   **Checksum Bits** (last 4 bits):
   `1011`

4. **Recompute the Checksum**: The entropy is converted back to bytes and hashed using SHA-256. Here’s how that works:
    - Convert entropy bits to bytes:
      `00000000000000000000100000000011000000001000000000101000000000110000000001110000000010000000001000000000101000000000`
      becomes the byte string (hexadecimal):
      `0000800302000a0607005002a00`
    - Hash the entropy using SHA-256:
      `SHA-256 hash of entropy: d7c30cd1f41a1fd4f0bc805df0289c4e26e64a049b54b4d56c3f0a160a41a7c8`
    - Take the first 4 bits of the hash (because our checksum is 4 bits for a 12-word seed phrase):
      `Recomputed checksum: 1101`

5. **Compare the Original and Recomputed Checksum**:
    - Original checksum: `1011`
    - Recomputed checksum: `1101`

   **Result**: The checksum does not match, so the seed phrase is **invalid**.

---

### Invalid Seed Phrase Example:

Let’s try an invalid seed phrase (manually constructed):
`"ability abandon absurd access accident about absorb abstract abuse absent above able"`

1. **Convert Seed Words to Indices**:
    * `ability`: index 1
    * `abandon`: index 0
    * `absurd`: index 8
    * `access`: index 10
    * `accident`: index 11
    * `about`: index 3
    * `absorb`: index 6
    * `abstract`: index 7
    * `abuse`: index 9
    * `absent`: index 5
    * `above`: index 4
    * `able`: index 2

   **Resulting Indices**:
   `[1, 0, 8, 10, 11, 3, 6, 7, 9, 5, 4, 2]`

2. **Convert Indices to Binary**:
    * `ability`: `00000000001`
    * `abandon`: `00000000000`
    * `absurd`: `00000001000`
    * `access`: `00000001010`
    * `accident`: `00000001011`
    * `about`: `00000000011`
    * `absorb`: `00000000110`
    * `abstract`: `00000000111`
    * `abuse`: `00000001001`
    * `absent`: `00000000101`
    * `above`: `00000000100`
    * `able`: `00000000010`

   **Concatenated Binary String**:
   `000000000010000000000000000010100000001011000000001100000001011000000001100000000111000000100000000011110000001101`

3. **Split the Binary Data**:
    - **Entropy** (128 bits):
      `00000000001000000000000000001010000000101100000000110000000101100000000110000000011100000010000000001111000000110`
    - **Checksum** (last 4 bits):
      `1011`

4. **Recompute the Checksum**:
    - Convert the entropy to bytes and hash with SHA-256:
      `SHA-256 hash: 68b36e61c7c97d6e7d78eb5f52b5dce60fa8f902b28a20f8a2a65c1bc012f73a`
    - Take the first 4 bits of the hash:
      `Recomputed checksum: 0110`

5. **Compare the Original and Recomputed Checksum**:
    - Original checksum: `1011`
    - Recomputed checksum: `0110`

   **Result**: The checksum does not match, so this seed phrase is **invalid**.

---

## Fraction of Possible Combinations that are Valid Seed Phrases

While there are many possible combinations of words from the BIP-39 wordlist, only a small fraction of these are valid seed phrases due to the checksum mechanism.

### Word Count and Entropy

BIP-39 seed phrases can have different lengths, each associated with a specific amount of entropy and a corresponding checksum.

| Seed Phrase Length | Entropy Length | Checksum Length | Total Length (Entropy + Checksum) |
|--------------------|----------------|-----------------|-----------------------------------|
| 12 words           | 128 bits       | 4 bits          | 132 bits                          |
| 15 words           | 160 bits       | 5 bits          | 165 bits                          |
| 18 words           | 192 bits       | 6 bits          | 198 bits                          |
| 21 words           | 224 bits       | 7 bits          | 231 bits                          |
| 24 words           | 256 bits       | 8 bits          | 264 bits                          |

### Why Only a Fraction are Valid

For each seed phrase, the checksum is computed from the entropy and appended to it. This checksum ensures that not every combination of BIP-39 words is valid—only those combinations where the checksum matches the entropy are considered valid.

The size of the checksum determines how many combinations of words are valid out of all the possible combinations.

- **12-word seed phrase**: Only 1 in 16 (2^4) possible combinations of words are valid.
- **15-word seed phrase**: Only 1 in 32 (2^5) possible combinations are valid.
- **18-word seed phrase**: Only 1 in 64 (2^6) possible combinations are valid.
- **21-word seed phrase**: Only 1 in 128 (2^7) possible combinations are valid.
- **24-word seed phrase**: Only 1 in 256 (2^8) possible combinations are valid.

### Example Calculation for a 12-Word Seed Phrase:

- The BIP-39 wordlist contains 2048 words.
- For a 12-word seed phrase, there are \(2048^{12}\) total possible combinations of words, which equals approximately \( 10^{39} \) combinations.
- However, due to the 4-bit checksum, only 1 out of every 16 combinations is valid.

Thus, the number of **valid** 12-word seed phrases is:
\[
\frac{2048^{12}}{16} \approx 5.44 \times 10^{37}
\]

This ensures that even though there are many potential word combinations, the checksum mechanism drastically reduces the number of valid seed phrases, making it harder to randomly generate a valid one.

### Key Takeaways:

- Even if the seed phrase contains valid BIP-39 words, the **checksum** is crucial for ensuring the integrity of the phrase.
- In both cases, we manually recomputed the checksum from the entropy and compared it to the original checksum.
- The checksum mismatch indicates that the seed phrase is **invalid**.
- The checksum mechanism in BIP-39 ensures that only a small fraction of possible combinations are valid seed phrases, significantly enhancing security by preventing random or malformed seed phrases from being used.