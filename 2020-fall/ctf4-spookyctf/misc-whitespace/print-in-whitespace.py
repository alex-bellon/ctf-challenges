
plain = input("Enter the phrase you want to print:")
output = open("whitespace.txt", "w")
curr = ""

for letter in plain:
    binary = "{0:b}".format(ord(letter))
    print(binary)
    curr += "1 0 1 1 10 "
    for bit in binary:
        if(bit == '1'):
            curr += "0\t"
        if(bit == '0'):
            curr += "1 "
    curr += "0\n1\t\n"

curr += "1 1 \n\n"

output.write(curr)
