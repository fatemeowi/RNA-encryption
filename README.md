# RNA Encryption

An experimental text encoding and decoding project written in Python.

## Overview

This project explores a custom data transformation algorithm that represents binary data using RNA codons.

The algorithm combines several operations:

- Text-to-binary conversion
- Binary-to-RNA codon mapping
- XOR-based bitwise transformation
- Random RNA sequence insertion
- Chunk-based codon reversal
- Decryption and message reconstruction

## How It Works

1. Convert the input message and key into binary.
2. Apply an XOR transformation to the binary data.
3. Map six-bit chunks to RNA codons.
4. Insert a random RNA sequence.
5. Reverse codon order within fixed-size chunks.
6. Reverse the operations to reconstruct the original message.

## Requirements

- Python 3
- No external libraries required

## How to Run

Clone the repository and navigate to the project directory.

Run the program:

```bash
python main.py
```

Choose an operation from the interactive menu:

- `1` — Encrypt a message
- `2` — Decrypt a message

Keep the key and the insertion metadata (`pos` and `insert_length`) to decrypt the encoded output.

## Disclaimer

This is an experimental educational project, not a secure encryption system. It has not been audited for cryptographic security.

## Author

Fatemeh (Mira)
