# Bookworm
* **Event:** ForeverCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
Based on the challenge prompt, you should figure out that you need to use the book linked in the prompt to help you decipher the message.

#### Step 2
This is a [book cipher](https://en.wikipedia.org/wiki/Book_cipher). The `CHA:PAR:LIN:WOR` refers to how you recover the words for the flag from the numbers - Chapter, Paragraph, Line, Word. If you calculate that out you get:
```
C  P  L  W
30 01 11 04 reading
39 08 02 08 is
51 07 05 11 fun
```
and the flag is `utflag{reading_is_fun}`.
