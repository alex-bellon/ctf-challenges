# John The Zipper
* **Event:** HackTXCTF 2019
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** `fcrackzip`, `hashcat` or John the Ripper

## Steps​
#### Step 1
The prompt says that I added a password to this ZIP archive, so the goal is to get the password and open the archive. While the intention of the problem was to do this with John the Ripper (hence the name), a couple of people were having issues getting John to work. In the end, many people used `fcrackzip`, which was confirmed to work.

#### Step 2
Using your preferred method of ZIP password cracking, you can determine that the password was `homework3`. If you type this in and open the ZIP archive, you can see the flag in one of the contained images: `utflag{z1p_z1p_h00ray}`.
