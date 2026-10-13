import random

# ==============================
# 1) CODON TABLE
# ==============================
CODONS = [
    'AAA','AAC','AAG','AAU','ACA','ACC','ACG','ACU',
    'AGA','AGC','AGG','AGU','AUA','AUC','AUG','AUU',
    'CAA','CAC','CAG','CAU','CCA','CCC','CCG','CCU',
    'CGA','CGC','CGG','CGU','CUA','CUC','CUG','CUU',
    'GAA','GAC','GAG','GAU','GCA','GCC','GCG','GCU',
    'GGA','GGC','GGG','GGU','GUA','GUC','GUG','GUU',
    'UAA','UAC','UAG','UAU','UCA','UCC','UCG','UCU',
    'UGA','UGC','UGG','UGU','UUA','UUC','UUG','UUU'
]

CODON_TO_INDEX = {c:i for i,c in enumerate(CODONS)}

# ==============================
# 2) TEXT TO BINARY
# ==============================
def text_to_binary(s):
    return ''.join(f"{ord(ch):08b}" for ch in s)

def binary_to_text(b):
    return ''.join(chr(int(b[i:i+8],2)) for i in range(0,len(b),8))

# ==============================
# 3) BINARY TO RNA
# ==============================
def binary_to_rna(b):
    out=[]
    for i in range(0,len(b),6):
        chunk=b[i:i+6]
        if len(chunk)<6:
            chunk=chunk.ljust(6,'0')
        idx=int(chunk,2)
        out.append(CODONS[idx])
    return ''.join(out)

def rna_to_binary(rna):
    bins=[]
    for i in range(0,len(rna),3):
        codon=rna[i:i+3]
        idx=CODON_TO_INDEX[codon]
        bins.append(f"{idx:06b}")
    return ''.join(bins)

# ==============================
# 4) XOR
# ==============================
def xor_bits(a,b):
    if len(a)<len(b):
        a=a.ljust(len(b),'0')
    if len(b)<len(a):
        b=b.ljust(len(a),'0')
    return ''.join('1' if x!=y else '0' for x,y in zip(a,b))

# ==============================
# 5) RANDOM RNA
# ==============================
NUC = ['A','C','G','U']
def random_rna(n):
    return ''.join(random.choice(NUC) for _ in range(n))

# ==============================
# 6) CHUNK-REVERSE
# ==============================
def chunk_reverse(rna, chunk_codons=5):
    codons=[rna[i:i+3] for i in range(0,len(rna),3)]
    out=[]
    for i in range(0,len(codons),chunk_codons):
        block=codons[i:i+chunk_codons]
        out.extend(block[::-1])
    return ''.join(out)

def chunk_reverse_back(rna, chunk_codons=5):
    return chunk_reverse(rna, chunk_codons)

# ==============================
# 7) ENCRYPT
# ==============================
def encrypt(msg, key):

    b  = text_to_binary(msg)
    bk = text_to_binary(key)

    bx = xor_bits(b,bk)

    rna = binary_to_rna(bx)

    # RANDOM INSERT at codon boundary
    insert_len = random.randint(10,25)
    insert_rna = random_rna(insert_len)

    codons = len(rna)//3
    pos_index = random.randint(0, codons)
    pos = pos_index * 3   # SAFE

    rna2 = rna[:pos] + insert_rna + rna[pos:]

    # chunk reverse safe
    rna3 = chunk_reverse(rna2, 5)

    return rna3, pos, insert_len

# ==============================
# 8) DECRYPT
# ==============================
def decrypt(enc, key, pos, insert_len):

    rna2 = chunk_reverse_back(enc,5)
    rna  = rna2[:pos] + rna2[pos+insert_len:]

    bx = rna_to_binary(rna)
    bk = text_to_binary(key)

    b = xor_bits(bx,bk)
    return binary_to_text(b)

# ==============================
# 9) INTERACTIVE MENU
# ==============================
if __name__ == "__main__":
    print("Choose operation:")
    print("1) Encrypt")
    print("2) Decrypt")
    ch = input("> ")

    if ch == "1":
        msg = input("Enter message: ")
        key = input("Enter key: ")

        enc, pos, ins = encrypt(msg, key)

        print("\n=== ENCRYPTED ===")
        print("RNA:", enc)
        print("pos:", pos)
        print("insert_length:", ins)
        print("=================")

    elif ch == "2":
        enc = input("Enter RNA sequence: ").strip()
        key = input("Enter key: ")
        pos = int(input("Enter pos: "))
        ins = int(input("Enter insert_length: "))

        dec = decrypt(enc, key, pos, ins)

        print("\n=== DECRYPTED ===")
        print("Message:", dec)
        print("=================")

    else:
        print("Invalid choice.")

# ==============================
#  MADE BY FATEMEH (mira) ₍^. .^₎⟆
# ==============================