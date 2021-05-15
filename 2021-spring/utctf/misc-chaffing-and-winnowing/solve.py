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
