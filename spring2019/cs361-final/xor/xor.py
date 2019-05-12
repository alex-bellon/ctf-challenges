flag = bytes('utflag{th3_p3n_is_mighti3r_th@n_th3_xor}'.encode('utf-8'))
key = bytes('s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3t'.encode('utf-8'))
result = ''

for i in range(len(flag)):
    result += chr(flag[i] ^ key[i])

print(bytes(result.encode('utf-8')))

cipher = bytes('\x06G\x05\x1eR\x13\x08G\x0bAl\x04@]<\x1b@+\x1eZ\x04\x1aG\x1d@A<\x06[4\x1dl\x17\x1a\x00+\x0b\\\x11\x0f'.encode('utf-8'))
plain = ''

for i in range(len(cipher)):
    plain += chr(cipher[i] ^ key[i])

print()
print(bytes(plain.encode('utf-8')))
