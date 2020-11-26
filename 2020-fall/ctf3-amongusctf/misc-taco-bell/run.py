import random

valid = open('/valid.txt', 'r').read().split('\n')[:-1]
invalid = open('/invalid.txt', 'r').read().split('\n')[:-1]

print('Task: please tell me whether or not these Taco Bell survey codes are valid. You must reply correctly 1000 times to complete the task. Just respond \'y\' if the code is valid or \'n\' if it isn\'t. Easy enough, right?\n')

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

print('Congrats! Here\'s the flag: utflag{blue_was_not_the_impostor}')
