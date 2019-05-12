
plain = input("Enter the phrase you want to print:")
output = open("whitespace.txt", "w")
curr = ""

for letter in plain:
    binary = "{0:b}".format(ord(letter))
    print(binary)
    curr += ". . . . . ."
    for bit in binary:
        if(bit == '1'):
            curr += ".\t"
        if(bit == '0'):
            curr += ". "
    curr += ".\n.\t.\n"

curr += ". . .\n"

output.write(curr)
