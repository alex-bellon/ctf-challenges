import hashlib, hmac, random, pprint, secrets

def dh(mod, base, a_secret, b_secret):

    a_public = (base ** a_secret) % mod
    b_public = (base ** b_secret) % mod

    shared = (b_public ** a_secret) % mod

    return shared, a_public, b_public

def make_wheat(message, key):

    result = list()

    key = key.to_bytes((key.bit_length() + 7) // 8, 'big')
    print(key)

    binary = ''.join(format(ord(x) , 'b').zfill(8) for x in message)

    for i in range(len(binary)):
        serial = i
        char = int(binary[i])

        data = bytes([serial]) + bytes([char]) # only works because these numbers are < 255

        h = hmac.new(key, data, hashlib.md5)
        mac = h.digest().hex()

        result.append((serial, char, mac))

    return result

def add_chaff(wheat):

    result = list()

    for entry in wheat:
        serial = entry[0]
        char = 1 ^ int(entry[1])
        mac = secrets.token_hex(16)

        result.append((serial, char, mac))

    return result + wheat

def main():

    mod = 78787
    base = 16405
    a = 3784
    b = 39583
    shared, a_public, b_public = dh(mod, base, a, b)

    print(shared, a_public, b_public)

    message = "cream_of_the_crop_29074"
    wheat = make_wheat(message, shared)

    output = add_chaff(wheat)
    output.sort()

    output_file = open('output.txt', 'w')
    wheat_file = open('wheat.txt', 'w')

    for entry in wheat:
        wheat_file.write(str(entry) + '\n')

    for entry in output:
        output_file.write(str(entry) + '\n')

    output_file.close()
    wheat_file.close()

main()
