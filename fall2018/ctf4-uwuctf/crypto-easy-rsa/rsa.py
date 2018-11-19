def ascii2int(string):
    textint = 0
    for char in string:
        textint = textint * 256 + ord(char)
    return(textint)

def int2ascii(integer):
    newtext = ""
    while integer > 0:
        currentchar = integer % 256
        newtext = chr(currentchar) + newtext
        integer -= currentchar
        integer = integer // 256
    return(newtext)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

keysize = 256 
p = 78615231505791119778531679171954912116516772172405580837835038280745008520119
q = 70057651003046527661678151293247823379678754249928504243640950278981509215109
n = p * q
phi = (p - 1) * (q - 1)
#e = 0x10000000000000001
e = 65537
#e = 18446744073709551617
d = int(modinv(e, phi))

print('p:  ' + str(p))
print('q:  ' + str(q))
print('n:  ' + str(n))
print('phi:  ' + str(phi))
print('e:  ' + str(e))
print('d:  ' + str(d))

print((e * d)%phi)

cleartext = input("enter text to encrypt (encoded length must be less than keysize): ")
m = ascii2int(cleartext)
print("\nencoded cleartext as integer m: %s" % format(m, 'x'))

c = pow(m, e, n)
print("\nciphertext (m ^ e mod n): %s" % format(c, 'x'))

newclearint = pow(c, d, n)
print("decrypted ciphertext as int (c ^ d mod n): %s" % format(newclearint, 'x'))
print("decrypted ciphertext: %s" % int2ascii(newclearint))
