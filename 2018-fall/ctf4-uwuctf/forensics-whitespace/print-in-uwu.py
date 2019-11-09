
plain = input("Enter the phrase you want to print:")
output = open("uwu.txt", "w")
curr = ""

for letter in plain:
    binary = "{0:b}".format(ord(letter))
    print(binary)
    curr += "UwU uwu uwu OwO  (◡w◡) "
    for bit in binary:
        if(bit == '1'):
            curr += "(UᵕU❁)\t"
        if(bit == '0'):
            curr += "(ᴜωᴜ) "
    curr += "(ᵘʷᵘ)\nuwu\t\n"

curr += "OwO uwu \n\n"

output.write(curr)
