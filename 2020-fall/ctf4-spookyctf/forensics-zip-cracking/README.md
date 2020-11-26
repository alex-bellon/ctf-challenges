# Unzipped
* **Event:** SpookyCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** `fcrackzip`, `hashcat` or John the Ripper


## Steps
#### Step 1
The goal of this challenge is to get the password and open the archive, which can be done with programs like [`fcrackzip`](https://github.com/hyc/fcrackzip), [`hashcat`](https://hashcat.net/hashcat/), or [John the Ripper](https://www.openwall.com/john/) and a [nice password list](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials).

#### Step 2
Using your preferred method of ZIP password cracking, you can determine that the password was `pumpkin`. If you type this in and open the ZIP archive, you can see the flag in one of the contained images: `utflag{lets_get_zip_cracking}`.
