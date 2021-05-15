flag = bytes('utflag{keep_it_on_repeat}'.encode('utf-8'))
key =  bytes('goatgoatgoatgoatgoatgoatg'.encode('utf-8'))
result = ''

for i in range(len(flag)):
    result += chr(flag[i] ^ key[i])

print(bytes(result.encode('utf-8')).hex())
print(bytes(result.encode('utf-8')))

cipher = bytes('\x12\x1b\x07\x18\x06\x08\x1a\x1f\x02\n\x11+\x0e\x1b>\x1b\t0\x13\x11\x17\n\x00\x00\x1a'.encode('utf-8'))
plain = ''

for i in range(len(cipher)):
    plain += chr(cipher[i] ^ key[i])

print()
print(bytes(plain.encode('utf-8')))
