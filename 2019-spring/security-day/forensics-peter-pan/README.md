# Peter Pan 
* **Event:** Security Day
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
You are given `peter-pan.txt`, which seems to contain the book Peter Pan. If you look closely, you will see that there are some extra characters, which all seem to be semicolons.

#### Step 2
If you actually look at the Unicode code for the characters though, they are a combination of semicolons and [Greek question marks](https://en.wikipedia.org/wiki/Question_mark#Greek_question_mark). Since there are only 2 types of characters, you can collect all of them, and interpret them as binary to get: `utflag{0n3s_@nd_z3er03s_@r3_l@m3}`.
