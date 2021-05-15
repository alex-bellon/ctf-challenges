from pwn import *
import json, math

r = remote('crypto.utctf.live', 1234)
#r = remote('localhost', 1234)

def line(until):
    a = r.recvuntil(until).decode('utf-8')
    print(a)
    return a

# Intro
line(':')

qubits = 30
epsilon = 0.01
iterations = int(math.pi / (2 * epsilon))

qubit = ''

for i in range(qubits):

    # Choose work with a qubit
    r.sendline('a')
    line(':')
    r.sendline(str(i))
    line(':')

    # Iterations to eliminate +
    for _ in range(iterations):
        r.sendline(str('e')) # Rotation
        line(':')
        r.sendline(str(epsilon)) # Send angle
        line(':')
        r.sendline('f') # CNOT
        line(':')
        r.sendline('h') # Bank verify
        line(':')

    r.sendline('k')

    s = r.recvuntil(':').decode('utf-8')
    measurement = s.split('as a ')[1][0]

    if measurement == '1':
        qubit += '+'
        continue

    # Choose work with a qubit
    r.sendline('a')
    line(':')
    r.sendline(str(i))
    line(':')

    # Iterations to eliminate -
    for _ in range(iterations):
        r.sendline(str('e')) # Rotation
        line(':')
        r.sendline(str(epsilon)) # Send angle
        line(':')
        r.sendline('g') # CNOT-X
        line(':')
        r.sendline('h') # Bank verify
        line(':')

    r.sendline('k')

    s = r.recvuntil(':').decode('utf-8')
    measurement = s.split('as a ')[1][0]

    if measurement == '1':
        qubit += '-'
        continue

    # Choose work with a qubit
    r.sendline('a')
    line(':')
    r.sendline(str(i))
    line(':')
    r.sendline('i')

    s = r.recvuntil(':').decode('utf-8')
    measurement = s.split('as a ')[1][0]

    qubit += measurement

print(qubit)

r.sendline('b')
line(':')
r.sendline(qubit)
print(line('}'))
