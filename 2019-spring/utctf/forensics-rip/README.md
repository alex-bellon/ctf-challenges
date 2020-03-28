# RIP
* **Event:** UTCTF 2019
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to open the ZIP file, you'll see that there is a password on it. You can use a tool like [John the Ripper](https://www.openwall.com/john/) or `hashcat` to crack the password. While the password is not in the top 10,000,000, it's one of those passwords + a simple modifier (a number in this case): `minicooper3`.

#### Step 2
If you `grep` for the flag, you will find it in the unzipped files: `utflag{m1n1_c00p3r_f4n}`.
