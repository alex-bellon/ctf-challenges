import random

alpha = 'abcdefghijklmnopqrstuvwxyz'
sub = ''.join(random.sample(alpha, len(alpha)))
plain = input('Input plaintext (only lowercase, numbers, curly brackets, and underscore): ')
cipher = ''

for letter in plain:
    if letter not in sub:
        cipher += letter
    else:
        cipher += sub[alpha.find(letter)]

print(alpha)
print(sub)
print()
print(cipher)
