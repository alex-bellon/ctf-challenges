import random, math
from sympy import symbols

# 14776336
#  5398021

s = 5398021 # secret
n = 5       # shares
k = 3       # threshold

coeff = list()
limit = 50
for i in range(k - 1):
    coeff.append(random.randint(-limit, limit))

x = symbols('x')
exp = s
power = 1

for c in coeff:
    exp += x**power * c
    power += 1

print(exp)

shares = list()
for share in range(1, n + 1):
    shares.append((share, exp.subs(x, share)))

print(shares)
