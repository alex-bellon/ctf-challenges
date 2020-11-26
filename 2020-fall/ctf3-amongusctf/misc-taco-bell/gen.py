import random

def format(num):
    result = ''
    num = str(num)
    for x in range(len(num)):
        if x % 4 == 0 and x:
           result += '-'
        result += num[x]

    return result

def check_card(card, valid, invalid):

    assert(len(str(card)) == 16)

    numbers = list(reversed([int(x) for x in str(card)]))
    for i in range(1, len(numbers)):
        if i % 2: # even index in 1-indexed array
            double = numbers[i] * 2
            numbers[i] = sum([int(i) for i in str(double)])
      
    total = sum(numbers)
    formatted = format(card)

    if total % 10 == 0:
        valid.write(formatted + '\n')
        print("VALID: " + formatted)
    else:
        invalid.write(formatted + '\n')
        print("INVALID: " + formatted)

def main():
    min = 1000000000000000
    max = 9999999999999999
    valid = open("valid.txt", "w")
    invalid = open("invalid.txt", "w")
    
    for i in range(100000):
        card = random.randint(min, max)
        solved = check_card(card, valid, invalid)

main()
