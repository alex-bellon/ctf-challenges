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
    a = "MY FAVORITE RICK IS TINY RICK!"
    b = "NO PICKLE RICK IS THE BEST ONE"
    p = "utctf{b0th_r1cks_@r3_t3rr1bl3}"

    aCipher = xorstrings(a, p)
    bCipher = xorstrings(b, p)

    print("Encoded A: " + aCipher.hex())
    print("Encoded B:" + bCipher.hex())
    
    print("")
    
    aHex = xorstrings(aCipher.decode('ascii'), p)
    bHex = xorstrings(bCipher.decode('ascii'), p)

    print("Original A: " + aHex.hex())
    print("Original B: " + bHex.hex())
    
    print("")
    
    print("A XOR A: " + xorstrings(aCipher.decode('ascii'), a).hex())
    print("B XOR B: " + xorstrings(bCipher.decode('ascii'), b).hex())

main()
