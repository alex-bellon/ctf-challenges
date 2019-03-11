import random

series = [0, 1, 2, 4, 5, 7, 9, 12, 13, 15, 17, 20, 22, 25, 28, 32, 33, 35, 37, 40, 42, 45, 48, 52, 54, 57, 60, 64, 67, 71, 75, 80, 81, 83, 85, 88, 90, 93, 96, 100, 102, 105, 108, 112, 115, 119, 123, 128, 130, 133, 136, 140, 143, 147, 151, 156, 159, 163, 167, 172, 176, 181, 186]
engChar = dict()
charEng = dict()

def fillDict():
    base = 0x3400
    for i in range(0x61, 0x7e):
        index = base + series[i - 0x61]
        print(str(i-97) + ' ' + str(chr(i)) + ' ' + str(index) + " " + str(hex(index)))
        engChar[i] = chr(index)
        charEng[chr(index)] = i
        base += 1

def encode(plain):
    result = ''
    plain = plain.lower()
    for letter in plain:
        print(str(ord(letter)) + " " + str(engChar[ord(letter)]))
        result += engChar[ord(letter)]
        num = engChar[ord(letter)]
    return result

def decode(cipher):
    result = ''
    for letter in cipher:
        result += chr(charEng[letter])
    return result

def embed(cipher):
    book = open('tale-of-two-cities.txt', 'r+')
    length = len(cipher)
    pos = 0
    for i in range(0, length):
        pos += random.randint(1000, 9999)
        book.seek(pos)
        book.write(cipher[i])
    book.write("Offset: 0x3400")
    book.close()

def main():
    fillDict()
    choice = input('[E]ncode or [D]ecode? ')
    if choice == 'E' or choice == 'e':
        plain = input('Input plaintext: ')
        cipher = encode(plain)
        embed(cipher)
    elif choice == 'D' or choice == 'd':
        cipher = input('Input ciphertext: \n')
        print(decode(cipher))

main()
