zwsp = '\u200B' # 0
zwnj = '\u200C' # 1

def encode():
    out = open('result.txt', 'w')
    cover = input('Input the string you want to use as cover: ')
    plain = input('Input the string you want to embed: ')
    binary = ''.join(format(ord(x) , 'b').zfill(8) for x in plain).replace('0', zwsp).replace('1', zwnj)
    third = int(len(cover) / 3)
    half = int(len(binary) / 2)
    result = cover[:third] + binary[:half] + cover[third:2 * third] + binary[half:] + cover[2 * third:]
    out.write(result)

def decode():
    cipher = input('Input the string with the cipher: ')

def main():
    choice = input('Would you like to [e]ncode or [d]ecode? ')
    if choice.lower() == 'e':
        encode()
    if choice.lower() == 'd':
        decode()

encode()
