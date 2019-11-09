text = input('Text to encode: ')

binary = list()
for letter in text:
    binary.append(format(ord(letter) , 'b').zfill(8))

count = len(binary)
print('┏━━━━━━━━┓')
while(count):
    result = '┃'
    for num in str(binary[count - 1]):
        if int(num):
            result += '█'
        else:
            result += ' '
    result += '┃'
    print(result)
    count -= 1
print('┗━━━━━━━━┛')
