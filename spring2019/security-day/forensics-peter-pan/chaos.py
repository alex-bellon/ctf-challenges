import random

def encode(plain):
    binary = ''.join(format(ord(x) , 'b').zfill(8) for x in plain)
    result = ''
    for num in binary:
        if int(num):
            result += '\u037E'
        if not int(num):
            result += ';'
    return result

def embed(cipher):
    book = open('peter-pan.txt', 'r+')
    book.seek(random.randint(50000, 100000))
    book.write('\n' + cipher + '\n')
    book.close()

def main():
    embed(encode(input('Word to hide: ')))

main()
