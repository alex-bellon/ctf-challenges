# OTP
* **Event:** CS361 Practice
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
From the title of the challenge, as well as the prompt, you should be able to figure out that this is a [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad). Since the key was reused, you can use [cribdragging](https://toolbox.lotusfa.com/crib_drag/) to guess the plaintexts.

#### Step 2
After recovering the plaintexts (`THE BEST FLAVOR OF ICE CREAM IS MINT CHOCOLATE` and `NO WAY THE BEST ICE CREAM FLAVOR IS STRAWBERRY`), you can XOR one of the plaintext/ciphertext pairs together to get the flag: `utflag{what_is_crib_dragging_anyways}`.
