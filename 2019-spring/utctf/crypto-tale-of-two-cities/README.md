# Tale of Two Cities 
* **Event:** UTCTF 2019
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
As the prompt suggests, there are extra characters inside the text file: a bunch of Chinese characters and `Offset: 0x340011`. The hint also tells you that you need the [OEIS](https://oeis.org/) sequence A000788.

#### Step 2
If you collect all of the characters, you get `㐾㐻㐌㐟㐀㐏㑖㐄㐓㐀㐴㐀㐄㐻㐉㐴㐷㐻㐾㐇㑎㑟`. When you remove the Unicode offset, you get the characters (in decimal) `62, 59, 12, 31, 0, 15, 86, 4, 19, 0, 52, 0, 4, 59, 9, 52, 55, 59, 62, 7, 78, 95`.

#### Step 3
This doesn't decode to a valid flag, so now it's time to use the OEIS sequence. You can use the formula `encoded letter = index of letter (0-25) + OEIS[index of letter (0-25)]`. Once you reverse this, you can get the flag: `utflag{characterstudy}`.
