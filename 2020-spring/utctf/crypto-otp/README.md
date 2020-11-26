# One True Problem
* **Event:** UTCTF 2020
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**
​
## Steps​
#### Step 1
From the prompt and problem title, you should hopefully figure out that this problem is exploiting key reuse in a [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad) scheme. As the name of the scheme suggests, pads/keys should only be used once or else you can recover the key.

#### Step 2
You can then use an online tool like [this](https://toolbox.lotusfa.com/crib_drag/) (or any other crib dragging tool) to guess for words in the plaintexts. Since the prompt mentions that they are arguing about CTF categories, you can eventually guess that these are the two plaintext messages:

```
THE BEST CTF CATEGORY IS CRYPTOGRAPHY!
NO THE BEST ONE IS BINARY EXPLOITATION
```

#### Step 3
From there, you can get the key (which is the flag) by XORing the plaintext with the correct ciphertext (you might have to do a little trial and error here). Then you can get the key `utflag{tw0_tim3_p4ds}`.
