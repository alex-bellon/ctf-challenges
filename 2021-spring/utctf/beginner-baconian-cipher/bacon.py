alphabet = list()

def encode():
    a = input('What character or phrase do you want to represent the first typeface? ')
    b = input('What character or phrase do you want to represent the second typeface? ')
    fillAlphabet(a, b)
    plain = input('Please input your plaintext (A-Z only): ')
    plain = plain.lower()
    cipher = ''
    for letter in plain:
        if letter in ' {}[]_':
            cipher += letter
            continue
        index = ord(letter) - 97
        cipher += alphabet[index]
    print(cipher)

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

def main():
    while(1):
        choice = input('Encode or decode? [e/d] ')
        if choice == 'e' or choice == 'E':
            encode()
            break
        elif choice == 'd' or choise == 'D':
            decode()
            break
        else:
            print('Please choose [e] or [d]')
main()
