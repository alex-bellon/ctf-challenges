# Finding Nemo 
* **Event:** PixarCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to open `nemo.zip`, you will see that it is password protected. You can use something like `frcrackzip` to perform a dictionary attack: `fcrackzip -D -u -p dictionary.txt nemo.zip`

#### Step 2
Once you unzip the archive, you will see a file called `not-flag.txt`, which is indeed not the flag. If you open it up in `vim`, you will see a bunch of zero-width characters in there. You can use the tool [zwfp](https://github.com/vedhavyas/zwfp) to extract the flag: `utflag{whew_that_was_hard}`.
