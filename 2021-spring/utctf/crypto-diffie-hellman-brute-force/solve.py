for i in range(1,69691):
    if (1001 ** i) % 69691 == 17016:
        print(str((47643 ** i) % 69691))
        exit()
