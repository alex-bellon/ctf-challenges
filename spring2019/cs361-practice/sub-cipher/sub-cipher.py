import string
from random import shuffle

alphabet = list(string.ascii_lowercase)
scramble = list(string.ascii_lowercase)
shuffle(scramble)
dic = dict(zip(alphabet, scramble))

plain = input("Phrase to encode: ").lower()
result = ''
for letter in plain:
    if letter in alphabet:
        result += dic[letter]
    else:
        result += letter

print("\n" + result)
