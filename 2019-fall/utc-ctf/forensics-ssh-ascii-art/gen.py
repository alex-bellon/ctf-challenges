from pprint import pprint

def makeChunks(string, size):
    return [string[i:size + i] for i in range(0, len(string), size)]


def generateCommands(address):
    address = address.replace(':', '').lower()

    byteLength = 2
    bytes_ = makeChunks(address, byteLength)

    commands = list()
    for byte in bytes_:
        binary = bin(int(byte, 16))[2:].zfill(8)
        for crumb in reversed(makeChunks(binary, 2)):
            commands.append(int(crumb, 2))
    return commands


def makeGrid(height, width):
    grid = [[0 for w in range(width)] for h in range(height)]
    # index into 153 positions with pos = y * width + x
    return grid


def makeWalk(commands, grid):
    moves = [[-1, -1], # 00 up left
             [ 1, -1], # 01 up right
             [-1,  1], # 10 down left
             [ 1,  1]] # 11 down right

    current = [8, 4]
    grid[4][8] = 15 # mark start position

    for command in commands:
        move = list()
        if current == [0, 0]: # top left corner
            if command == 0: move = [0, 0]
            elif command == 1: move = [1, 0]
            elif command == 2: move = [0, 1]
            elif command == 3: move = moves[commmand]
        elif current == [16, 0]: # top right corner
            if command == 0: move = [-1, 0]
            elif command == 1: move = [0, 0]
            elif command == 2: move = moves[command]
            elif command == 3: move = [0, 1]
        elif current == [0, 8]: # bottom left corner
            if command == 0: move = [0, -1]
            elif command == 1: move = moves[command]
            elif command == 2: move = [0, 0]
            elif command == 3: move = [1, 0]
        elif current == [16, 8]: # bottom right corner
            if command == 0: move = moves[command]
            elif command == 1: move = [0, -1]
            elif command == 2: move = [-1, 0]
            elif command == 3: move = [0, 0]
        elif current[1] == 0: # top
            if command == 0: move = [-1, 0]
            elif command == 1: move = [1, 0]
            elif command == 2: move = moves[command]
            elif command == 3: move = moves[command]
        elif current[1] == 8: # bottom
            if command == 0: move = moves[command]
            elif command == 1: move = moves[command]
            elif command == 2: move = [-1, 0]
            elif command == 3: move = [1, 0]
        elif current[0] == 0: # left
            if command == 0: move = [0, -1]
            elif command == 1: move = moves[command]
            elif command == 2: move = [0, 1]
            elif command == 3: move = moves[command]
        elif current[0] == 16: # right
            if command == 0: move = moves[command]
            elif command == 1: move = [0, -1]
            elif command == 2: move = moves[command]
            elif command == 3: move = [0, 1]
        else:
            move = moves[command]

        current = [current[i] + move[i] for i in range(2)]
        grid[current[1]][current[0]] += 1

    grid[current[1]][current[0]] = 16
    return grid

def drawArt(grid):
    symbols = ' .o+=*BOX@%&#/^SE'
    print('+-----------------+')
    for row in grid:
        line = ''.join([symbols[row[i]] for i in range(len(row))])
        print('|' + line + '|')
    print('+-----------------+')


def main():
    address = input('Please input the fingerprint you want to convert: ')
    commands = generateCommands(address)
    grid = makeGrid(9, 17)
    grid = makeWalk(commands, grid)
    drawArt(grid)

main()
