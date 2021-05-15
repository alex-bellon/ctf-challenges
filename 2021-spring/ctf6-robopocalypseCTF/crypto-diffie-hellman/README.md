# DH-9000 
* **Event:** RobopocalypseCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The robots' new crypto scheme is just Diffie Hellman. Luckily for us, they chose a small p value, which means that we can use brute force to recover one of the secret values, and consequently the shared secret. 

#### Step 2
Basically, we can just try every value 1-8089 for one of the secret values. Here's a quick python script that will brute force the value of a and then calculate and print out the shared secret:

```python
for i in range(1,8090): # try all values 1-p
    if (823 ** i) % 8089 == 1228: # if g^i mod p = A
        print(str((6820 ** i) % 8089)) # print B^a mod p (the shared secret)
```

#### Step 3
When you figure out one of the secret values, you should be able to calculate the shared value/flag: `utflag{7999}`
