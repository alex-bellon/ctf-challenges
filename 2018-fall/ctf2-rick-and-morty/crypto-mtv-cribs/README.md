# MTV Cribs 
* **Event:** RickAndMortyCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
From the title of the challenge, as well as the prompt, you should be able to figure out that this is a [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad). Since the key was reused, you can use [cribdragging](https://toolbox.lotusfa.com/crib_drag/) to guess the plaintexts.

#### Step 2
After recovering the plaintexts (`MY FAVORITE RICK IS TINY RICK!` and `NO PICKLE RICK IS THE BEST ONE`), you can XOR one of the plaintext/ciphertext pairs together to get the flag: `utctf{b0th_r1cks_@r3_t3rr1bl3}`.
