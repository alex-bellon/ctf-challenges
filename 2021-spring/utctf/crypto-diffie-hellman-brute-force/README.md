# Small P Problems
* **Event:** UTCTF 2021
* **Problem Type:** Cryptography
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The crypto scheme in this problem is the [Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) (as hinted to by the names in the prompt and the variable labels). Luckily for us, the p value is small, which means that we can use brute force to recover one of the secret values, and consequently the shared secret.

#### Step 2
Basically, we can just try every value 1-8089 for one of the secret values. Here's a quick python script that will brute force the value of a and then calculate and print out the shared secret:

```python
for i in range(1,69691): # try all values 1-p
    if (1001 ** i) % 69691 == 17016: # if g^i mod p = A
        print(str((47643 ** i) % 69691)) # print B^a mod p (the shared secret)
        exit()
```

#### Step 3
When you figure out one of the secret values, you should be able to calculate the shared value/flag: `utflag{53919}`
