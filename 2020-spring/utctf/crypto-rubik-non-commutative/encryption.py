import random
import pprint

debug = 0
moves = ["F", "B", "U", "D", "L", "R", "F'", "B'", "U'", "D'", "L'", "R'"]

# please do not judge me for the utter trash this method is
def simplify(config):
    config = config.strip(' ')
    if debug: print("Orig: " + config)
    changed = 1
    while changed == 1:
        changed = 0
        moves = config.split(" ")
        newConfig = ""
        i = 0
        while i < len(moves):
            move = moves[i]
            if i < len(moves) - 1 and (moves[i+1] == move + "'" or moves[i+1] + "'" == move):
                if debug: print("Removing " + move + " and " + moves[i+1] + " at pos " + str(i) + " and " + str(i+1))
                i += 2
                changed = 1
            elif i < len(moves) - 2 and move == moves[i+1] and move == moves[i+2]:
                if debug: print("Removing " + move + " and " + moves[i+1] + " at pos " + str(i) + " and " + str(i+1))
                newConfig += move[:-1] + ' ' if "'" in move else move + "' " 
                i += 3
                changed = 1
            elif i < len(moves) - 1 and move == moves[i+1] and "'" in move:
                if debug: print("Removing " + move + " and " + moves[i+1] + " at pos " + str(i) + " and " + str(i+1))
                newConfig += move[:-1] + ' ' + move[:-1] + ' ' 
                i += 2
                changed = 1
            else:
                newConfig += move + ' '
                i += 1
        config = newConfig.strip(' ')
    return newConfig.strip(' ')

def computeInverse(config):
    result = ''
    moves = reversed(config.split(' '))
    for move in moves:
        if '\'' in move:
            result += move[0] + ' '
        else:
            result += move + '\' '
    return result.strip(' ')

def keyGen(configLength, numConfigs):
    pub = list()
    for i in range(numConfigs):
        config = ''
        for j in range(random.randint(2, configLength)):
            config += moves[random.randint(0, len(moves) - 1)] + ' '
        pub.append(config.strip(' '))

    privChoices = pub.copy()
    for config in pub:
        privChoices.append(computeInverse(config))
    oldPrivChoices = privChoices.copy()

    random.shuffle(privChoices)
    priv = privChoices[:numConfigs - 2]
    index = list()
    for config in priv:
        index.append(oldPrivChoices.index(config))
    prod = ' '.join(priv)
    return [pub, priv, index, prod]

def computeTransition(product, public):
    result = list()
    productInv = computeInverse(product).strip(' ')
    for config in public:
        elem = productInv + ' ' + config + ' ' + product
        result.append(elem)
    return result

def computeSecret(product, public, index, tuples, side):
    result = ''
    if side == 0: # Alice
        inverse = computeInverse(product)
        result += inverse + ' '
        for i in index:
            if i >= len(public): # One of the inverses
                result += computeInverse(tuples[i - len(public)]) + ' '
            else:
                result += tuples[i] + ' '
    elif side == 1: # Bob
        for i in index:
            if i >= len(public): # One of the inverses
                result += computeInverse(tuples[i - len(public)]) + ' '
            else:
                result += tuples[i] + ' '
        result = computeInverse(result.strip(' ')) + ' '
        result += product + ' '
    result = simplify(result)
    return result

def main():
    x = 3
    y = 4

    aKeys = keyGen(x, y)
    bKeys = keyGen(x, y)

    alicePub = aKeys[0]
    alicePriv = aKeys[1]
    aliceIndex = aKeys[2]
    A = aKeys[3]

    bobPub = bKeys[0]
    bobPriv = bKeys[1]
    bobIndex = bKeys[2]
    B = bKeys[3]

    print("Alice Keys: " + str(aKeys))
    print("Bob Keys: " + str(bKeys))

    aBar = computeTransition(A, bobPub)
    aBarSimp = [simplify(elem) for elem in aBar]
    
    bBar = computeTransition(B, alicePub)
    bBarSimp = [simplify(elem) for elem in bBar]

    print("Alice sends: " + str(aBarSimp))
    print("Bob sends: " + str(bBarSimp))
    
    sharedA = computeSecret(A, alicePub, aliceIndex, bBar, 0)
    sharedB = computeSecret(B, bobPub, bobIndex, aBar, 1)

    print("ShareA: " + sharedA)
    print("ShareB: " + sharedB)

main()
