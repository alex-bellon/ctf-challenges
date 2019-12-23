moves = input('Input moves (make sure 8|# moves): ')

binary = ''.join(bin(int(move))[2:].zfill(2) for move in moves)
print(len(binary))

result = ''

for i in range(0, len(binary), 8):
    char = binary[i:i+8]
    chunks = [char[i:i+2] for i in range(0, len(char), 2)]
    chunks.reverse()
    char = ''.join(chunks)
    print(char)
    result += hex(int(char, 2))[2:].zfill(2)

print(result)
