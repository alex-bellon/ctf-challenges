# XOR 
* **Event:** RobopocalypseCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
You are given a bunch of bytes, and based on the prompt you should be able to determine that the flag was "encrypted" by XORing it with something else. 

#### Step 2
Since you know that XOR inverts itself, and you know what the flag format is, you can try XORing the beginning of the flag (`utflag{`) with the ciphertext.

#### Step 3
When you do that, you will see that the other value we XORed with was `goat`, so you can just repeat that out until it is the length of the ciphertext and then XOR them together to get the flag: `utflag{keep_it_on_repeat}`.
