# Zeros and Ones
* **Event:** ForeverCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The flag is encoded in binary, since the ciphertext is only using 1s and 0s in groups of 8 (one for each character). We can use an online decoder like [this](https://www.rapidtables.com/convert/number/binary-to-ascii.html) to recover the flag: `utflag{zero_one_one_one_zero_zero_one_one}`.
