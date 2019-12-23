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
    a = "MY FAVORITE SEASON IS TOTALLY THE SUMMER"
    b = "NO WAY THE BEST SEASON IS TOTALLY SPRING"
    p = "utc{drag_those_cribs}utc{drag_those_crib"

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
