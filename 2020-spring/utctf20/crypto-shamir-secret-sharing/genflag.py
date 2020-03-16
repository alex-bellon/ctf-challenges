import itertools, string

def generate_strings(length):
    chars = string.ascii_letters + string.digits
    for item in itertools.product(chars, repeat = length):
        yield "".join(item)

def main():
    out = open("flags.txt", "w")
    gen = generate_strings(4)
    for string in gen:
        flag = "utflag{" + string + "}"
        print(flag)
        out.write(flag + "\n")
    out.close()

main()
