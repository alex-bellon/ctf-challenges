# Farmers Only
* **Event:** UTCTF 2021
* **Problem Type:** Miscellaneouss
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**


## Steps
#### Step 1
Hopefully through some internet searching of the phrases in the prompt (especially "confidentiality without encryption"), you should stumble upon [chaffing and winnowing](https://en.wikipedia.org/wiki/Chaffing_and_winnowing).

#### Step 2
The gist of how chaffing and winnowing works is that you are given a tuple of `(serial #, bit value, MAC value)`. For every serial number, there are two possible bit values but only one is correct. In order to tell which value is correct, you have to compute the MAC as a function of the `serial bit # || bit value` and see if it matches the given MAC.

#### Step 3
In this case, the MAC algorithm that is being used is HMAC-MD5 (as hinted to by the file name), and the secret key you use to calculate the HMAC is that given by the Diffie-Hellman key exchange detailed in the same file (you can calculate this shared key using the same technique you used in **Small P Problems**). My solve script for this challenge looks like this:

```python
import ast, hashlib, hmac
from Crypto.Util.number import long_to_bytes

for i in range(1,78787):
    if (16405 ** i) % 78787 == 59145:
        key = (18081 ** i) % 78787
        break

key = long_to_bytes(key)

entries = open('output.txt', 'r').read().split('\n')[:-1]

bitstring = ''

for entry in entries:
    entry = ast.literal_eval(entry)

    serial = entry[0]
    char = entry[1]

    data = bytes([serial]) + bytes([char])

    h = hmac.new(key, data, hashlib.md5)
    mac = h.digest().hex()

    if mac == entry[2]:
        bitstring += str(entry[1])

n = int(bitstring, 2)
flag = long_to_bytes(n).decode()

print(flag)
```

At the end, once you figure out which bits are valid and which aren't, you can convert it to ASCII to get the flag: `utflag{cream_of_the_crop_29074}`.
