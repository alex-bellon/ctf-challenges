# Sizzling Bacon
* **Event:** UTCTF 2021
* **Problem Type:** Beginner
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The prompt mentions the words "Francis" and "Bacon", and you are given some sort of encoded flag. If you do a little searching about Francis Bacon and encodings/ciphers, you should stumble upon [Bacon's cipher](https://en.wikipedia.org/wiki/Bacon%27s_cipher).

#### Step 2
In this case, the lowercase `s` represents a 0 and an uppercase `S` represents a 1 (if you weren't sure you could try it both ways). You can either decode the flag by hand or write a script to do it, like this one:

```python
def decode():
    a = input('What character or phrase represents the first typeface? ')
    b = input('What character or phrase represents the second typeface? ')
    fillAlphabet(a, b)
    cipher = input('Please input your ciphertext: ')
    cipher = cipher.replace(a, '1')
    cipher = cipher.replace(b, '0')
    plain = ''
    index = 0
    while index < len(cipher):
        if cipher[index] not in '01':
            plain += cipher[index]
            index += 1
            continue
        letter = cipher[index:index + 5]
        plain += chr(int(letter, 2) + 97)
        index += 5
    print(plain)

def fillAlphabet(a, b):
    for i in range (0, 26):
        binary = bin(i)[2:]
        if len(binary) < 5:
            temp = ''
            for pad in range (0, 5 - len(binary)):
                temp += '0'
            binary = temp + binary
        binary = binary.replace('1', a)
        binary = binary.replace('0', b)
        global alphabet
        alphabet.append(binary)

decode()
```

Whichever way you do it, you should be able to get the flag as the decoded message: `utflag{crispybaconcipher}`.
