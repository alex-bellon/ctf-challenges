import base64
from binascii import hexlify
import os
import struct

def xorstrings(a, b):
    result = b''
    for i in range(len(a)):
        result += struct.pack("B", (ord(a[i]) ^ ord(b[i])))
    return result

def main():
    a = "THE BEST CTF CATEGORY IS CRYPTOGRAPHY!"
    b = "NO THE BEST ONE IS BINARY EXPLOITATION"
    p = "utflag{tw0_tim3_p4ds}utflag{tw0_tim3_p"

    aCipher = xorstrings(a, p)
    bCipher = xorstrings(b, p)

    print("Encoded A: " + aCipher.hex())
    print("Encoded B: " + bCipher.hex())
    
    print("")
    
    aHex = xorstrings(aCipher.decode('utf8'), p)
    bHex = xorstrings(bCipher.decode('utf8'), p)

    print("Original A: " + aHex.hex())
    print("Original B: " + bHex.hex())
    
    print("")
    
    print("A XOR A: " + xorstrings(aCipher.decode('utf8'), a).hex())
    print("B XOR B: " + xorstrings(bCipher.decode('utf8'), b).hex())

main()
