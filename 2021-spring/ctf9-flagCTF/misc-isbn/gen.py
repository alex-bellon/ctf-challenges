import random

def format(num):
    num = str(num)
    return num[0] + '-' + num[1:4] + '-' + num[4:9] + '-' + num[9]

def check_isbn(isbn, valid, invalid):

    total = 0
    weight = 10
    for i in isbn:
        total += (int(i) * weight)
        weight -= 1

    formatted = format(isbn)

    if total % 11 == 0:
        valid.write(formatted + '\n')
        print("VALID: " + formatted)
    else:
        invalid.write(formatted + '\n')
        print("INVALID: " + formatted)

def main():
    min = 1000000000
    max = 9999999999
    valid = open("valid.txt", "w")
    invalid = open("invalid.txt", "w")
    
    for i in range(100000):
        isbn = random.randint(min, max)
        solved = check_isbn(str(isbn).zfill(10), valid, invalid)

main()
