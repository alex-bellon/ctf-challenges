
plain = input("Enter the phrase you want to print:")
output = open("whitespace.txt", "w")
curr = ""

for letter in plain:
    binary = "{0:b}".format(ord(letter))
    print(binary)
    curr += "- - - - (0 "
    for bit in binary:
        if(bit == '1'):
            curr += "1\t"
        if(bit == '0'):
            curr += "0 "
    curr += ")\nprint\t\n"

curr += "- - \n\n"

output.write(curr)
