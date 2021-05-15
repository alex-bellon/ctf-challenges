# Wiesner's Quantum Bank
* **Event:** UTCTF 2021
* **Problem Type:** Cryptography
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**


## Steps
#### Step 1
The title of the challenge and the intro paragraphs on the remote service should lead you to [Wiesner's quantum money scheme](https://en.wikipedia.org/wiki/Quantum_money). As the bank's interface mentions, in order to get the flag you need to correctly "guess" the state of the bank's single Schroedinger Buck. Given this is a CTF, you'll probably have to do some sort of attack to be able to recover the SB's state. If you do some searching about possible attacks on Wiesner's quantum money scheme, you should come across [this paper](https://arxiv.org/abs/1404.1507) that uses the [Elitzur-Vaidman bomb-testing method](https://en.wikipedia.org/wiki/Elitzur%E2%80%93Vaidman_bomb_tester) to recover the state of quantum money with a high probability.

#### Step 2
If you want to get into the nitty-gritty math details you're probably better off reading the paper, but here's the general gist of the attack for each qubit |Ψ_i⟩:

- Initialize your qubit to |0⟩
- Repeat π/(2 * ε) times:
  - Apply a rotation gate of angle ε to your qubit
  - Apply a CNOT gate to your qubit + the bank's qubit (your qubit is the control qubit)
  - Have the bank verify its qubit
- Measure your qubit in the {|0⟩, |1⟩} basis

Based on the measurement from your qubit, you will be able to tell whether the bank's qubit is |+⟩, because you will get a 1 as the measurement, while everything else will give you a 0. Therefore if you measure a 1, you know this is a |+⟩ qubit and can move on to the next qubit. Otherwise, continue on:

- Initialize your qubit to |0⟩
- Repeat π/(2 * ε) times:
  - Apply a rotation gate of angle ε to your qubit
  - Apply a CNOT-X gate to your qubit + the bank's qubit (your qubit is the control qubit)
  - Have the bank verify its qubit
- Measure your qubit in the {|0⟩, |1⟩} basis

Now for this round, if you measure a 1, you know your qubit is a |-⟩, and other wise it must be a |0⟩ or a |1⟩.

Finally, you can measure the bank's qubit in the {|0⟩, |1⟩} basis without fear of collapsing it to the wrong qubit, and determine whether it was a |0⟩ or a |1⟩.

When you perform this algorithm for every qubit of the bank's SB state, you should be able to recover all 30 qubits. You can then feed your recovered state into the service to get a flag in return: `utflag{quantum_bank_robber}`.

Here is my solver script implemented in Python. Probably not the most efficient or pretty thing, but it works :)

```python
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
```
