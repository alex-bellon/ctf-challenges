from math import gcd

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1): return x
    return -1

def encode():
    a = input('What coprime number do you want to use for a? ')
    while(gcd(int(a), 26) != 1):
        a = input('Sorry, that number is not coprime with 26. Please enter a different number: ')
    b = input('What number between 0-25 (inclusive) do you want to use for b? ')
    while(int(b) > 25 or int(b) < 0):
        b = input('Sorry, that number is not between 0-25. Please enter a number between 0-25 (inclusive): ')

    plain = input('Input your message using only letters [A-Z]: ').lower()
    a = int(a)
    b = int(b)
    cipher = ''
    for letter in plain:
        temp = chr((a * (ord(letter) - 97) + b) % 26 + 97)
        cipher += temp
    print("\n\t  :\n\t [\"]  -[ " + cipher + " ]\n\t/[_]\\\n\t ] [")

def decode():
    a = input('What coprime number do you want to use for a? ')
    while(gcd(int(a), 26) != 1):
        a = input('Sorry, that number is not coprime with 26. Please enter a different number: ')
    b = input('What number between 0-25 (inclusive) do you want to use for b? ')
    while(int(b) > 25 or int(b) < 0):
        b = input('Sorry, that number is not between 0-25. Please enter a number between 0-25 (inclusive): ')
    a = int(a)
    b = int(b)
    cipher = input('Input your ciphertext: ').lower()
    plain = ''
    for letter in cipher:
        temp = chr((modInverse(a, 26) * (ord(letter) - 97 - b)) % 26 + 97)
        plain += temp
    print("\n\t  :\n\t [\"]  -[ " + plain + " ]\n\t/[_]\\\n\t ] [")

def main():
    while(1):
        choice = input('\nEncode or decode? [e/d] ')
        if choice == 'e' or choice == 'E':
            encode()
            break
        elif choice == 'd' or choice == 'D':
            decode()
            break
        else:
            print('Please choose [e] or [d]')

main()
