# Not The Flag
* **Event:** CS361 Final
* **Problem Type:** Misc
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to copy and paste the given "flag", you will se that it doesn't work. However, if you open it up in something like `vim`, you will see that there are [Zero Width Characters](https://en.wikipedia.org/wiki/Zero-width_space) in between the letters. 

#### Step 2 
You should also notice that there are only 2 characters, and they repeat in a sort of pattern. If you put them all together, and switch the `\u200C`s for 1 and `\u200B` for 0, you will see that it's actually binary.

#### Step 3
You can then convert that binary to ASCII to get the flag: `utflag{but_i_am}`.
