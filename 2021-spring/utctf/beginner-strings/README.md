# Stringy Things
* **Event:** UTCTF 2021
* **Problem Type:** Beginner
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**


## Steps
#### Step 1
The prompt mentions that I "left a string" in this binary. This is referencing the commonly-used Linux/UNIX tool [`strings`](https://linux.die.net/man/1/strings) which will find any strings in the file you pass it.

#### Step 2
If you run `string calc`, you'll get a lot of extra stuff, so your best bet is to pipe it to grep to search the results of `strings` for `utflag`: `strings calc | grep utflag`. This should give you the flag: `utflag{strings_is_op}`.
