# Keep It Zipped 
* **Event:** CTF1
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to open the ZIP file, you'll see that there is a password on it. You can use a tool like [John the Ripper](https://www.openwall.com/john/) or `hashcat` to crack the password.

#### Step 2
If you `grep` for the flag, you will find it in the unzipped files: `utflag{d0wn_th3_r@bb1t_h0l3}`.
