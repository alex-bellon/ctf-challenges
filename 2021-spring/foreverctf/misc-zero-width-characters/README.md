# Nothing In Between
* **Event:** ForeverCTF
* **Problem Type:** Misc
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you try to copy the flag and submit it, it won't work. But, if you copy the flag into something like `vim` (or [this tool](http://unicode.scarfboy.com/), or [this tool](https://cryptii.com/pipes/unicode-lookup) or read the hint :) ) you will see that there are extra characters in there:

![](zwc.png)

#### Step 2
Those characters are [zero width characters](https://en.wikipedia.org/wiki/Zero-width_space) that cannot be seen when printed. You can see that there are two of them that are alternating: 200B (zero width space) and 200C (zero width non-joiner). If you replace all the 200B characters with 0 and the 200C characters with 1, the hidden text will now look a lot like binary that's representing ASCII characters.

#### Step 3

When you convert the binary to ASCII ([this tool is nice for that](https://www.rapidtables.com/convert/number/binary-to-ascii.html)), you should get the *real* flag: `utflag{you_cant_see_me}`.
