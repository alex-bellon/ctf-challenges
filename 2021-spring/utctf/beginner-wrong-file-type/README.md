# Magic Bytes
* **Event:** UTCTF 2021
* **Problem Type:** Forensics
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**
​

## Steps​
#### Step 1
If you try to open up the `out.txt`, you'll see that the file is just filled with random garbage. But, at the beginning of that random garbage is the string 'PNG'. Hopefully, this is where you realize that this is actually a .PNG file, but with the wrong file extension.

#### Step 2
The easiest way to fix this is to rename the file to `out.png`, and/or try to open the file with an image viewer. When you do open it, the image has the flag: `utflag{file_extensions_mean_nothing}`.
