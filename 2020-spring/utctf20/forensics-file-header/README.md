# The Legend of Hackerman, Pt. 1
* **Event:** UTCTF 2020
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**
​
## Steps​
#### Step 1
If you try to open up this image, you won't be able to, and you should be able to determine using a tool like `xxd` that something is wrong with bytes of the [file header](https://en.wikipedia.org/wiki/List_of_file_signatures).

#### Step 2
If you edit the hex of the file (using something like `bless`) and restore the file header, you should be able to open the file again and see the flag: `utflag{3lit3_h4ck3r}`.
