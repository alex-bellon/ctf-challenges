import random

valid = open('/valid.txt', 'r').read().split('\n')[:-1]
invalid = open('/invalid.txt', 'r').read().split('\n')[:-1]

flag = open('/flag.txt', 'r').read()

print('Can you make sure all of these ISBN numbers are valid for me? You must reply correctly 1000 times and then I\'ll give you a flag in return. Just respond \'y\' if the code is valid or \'n\' if it isn\'t. Easy enough, right?\n')

for i in range(1000):
    choice = random.randrange(10)
    if choice % 2:
        correct = 'y'
        print(random.choice(valid))
    else:
        correct = 'n'
        print(random.choice(invalid))
    
    response = input()

    if response != correct:
        print('You responded incorrectly. Goodbye.')
        exit()

print('Congrats! Here\'s the flag: ' + flag)
