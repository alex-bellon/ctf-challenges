# Secret Transmission
* **Event:** galacticBattleCTF
* **Problem Type:** Cryptography
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
As mentioned in the prompt, this is encoded with an [Affine cipher](https://en.wikipedia.org/wiki/Affine_cipher). You're not given the values of `a` or `b`, but luckily there are tools that can make our lives easier.

#### Step 2
You can use a tool like [this](https://www.dcode.fr/affine-cipher) to brute force all the possible combinations. When you plug in `uteontkfsdtfwtsfwfsd`, one of the most likely candidates will be the flag: `helpmedobieonebonobi`.
