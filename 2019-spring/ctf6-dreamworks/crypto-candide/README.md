# CPWL
* **Event:** DreamworksCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
Based on the challenge prompt, you should figure out that you need to use Project Gutenberg, a website that provides free eBooks. 19942 refers to the id of the book, and `https://www.gutenberg.org/ebooks/19942` leads to the book Candide by Voltaire.

#### Step 2
This is a [book cipher](https://en.wikipedia.org/wiki/Book_cipher). The challenge title (CPWL) refers to how you should find the letters of the flag: Chapter, Paragraph, Word, Letter. If you calculate that out you get:
```
  C  P  W  L
Y 28 04 17 01
A 19 10 06 04

L 09 07 11 04
I 15 03 14 02
K 23 12 29 02
E 01 08 02 02

J 14 07 15 01
A 22 02 06 02
Z 24 06 22 05
Z 07 03 02 04
```
and the flag is `ya like jazz`.
