# All Greek To Me
* **Event:** ForeverCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The flag is encoded with a [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), a [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher) that replaces each letter with another letter that is `x` places further down in the alphabet, where we call `x` the shift.

#### Step 2
Since there are only 26 possible unique shifts, and 1 is no shift which renders it basically useless, there are only 25 viable shifts. You can try each of these shifts out manually, or you can use an online tool like [this](https://cryptii.com/pipes/caesar-cipher) to recover the flag: `utflag{yet_another_caesar_pun}`.
