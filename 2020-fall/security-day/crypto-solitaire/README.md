# Pontifex
* **Event:** Security Day 2020
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
When you look up the title of the challenge, you should be led to the [Solitaire Cipher](https://en.wikipedia.org/wiki/Solitaire_%28cipher%29), also called the Pontifex cipher. This is a cipher that uses a deck of cards to encode a string of text. The twist here is that this deck doesn't have the traditional 52 cards, only 20 (which you can tell by length the array for the starting shuffle). This means you can't use an online tool to solve this :)

#### Step 2
Basically, the whole cryptosystem works the same as normal but there are only 20 cards, so the jokers represent values 21 and 22. This means you'll have to recreate the keystream yourself (you can see my implementation of the keystream generator in `solitaire.py`). Once you're able to recreate the keystream, then you can subtract those values from the numerical values of the characters in the ciphertext (modding by 26 when necessary). That should get you to the plaintext: `cupidshuffle` and therefore the flag: `utflag{cupidshuffle}`.
