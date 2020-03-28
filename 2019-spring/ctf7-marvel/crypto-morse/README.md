# Morse 
* **Event:** MarvelCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you look at the contents of `binary.txt`, it doesn't look like binary as there are values that are all 0s and they're all different lengths. You should notice that there are only 2 characters, and that the longest "word" is only 5 characters long. This all points to the fact that this is actually Morse code.

#### Step 2
You can then use an online tool like [this one](https://morsecode.world/international/translator.html) to convert the Morse code (although you may have to replace the 1s and 0s with dots and dashes). Then you will get the flag: `s0rryn0ts0rry`.
