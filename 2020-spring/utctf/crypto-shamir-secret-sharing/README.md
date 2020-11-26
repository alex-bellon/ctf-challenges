# Curveball
* **Event:** UTCTF 2020
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**
​

This problem was (supposed to be) a pretty simple Shamir's Secret Sharing problem. I decided relatively late into writing this problem that I would hash the points to add a little bit more difficulty. Clearly,

![](https://i.redd.it/xyc3mliaf0nz.jpg)

## Steps​
#### Step 1
From the prompt, you should be able to find out that this problem has to do with [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing). There are enough shares here to get the secret, so we can just plug and chug.

#### Step 2
The 3 hex tuples are hashes of the integer (x,y) points, and when you crack them on something like [crackstation](https://crackstation.net/), you get
```
(2, 5398141)
(3, 5398288)
(5, 5398756)
```

#### Step 3
Since we have three points, we can calculate the parabola that goes through all 3 points. I used [this online tool](https://www.analyzemath.com/parabola/three_points_para_calc.html), but Wolfram Alpha, Sage, etc. will work just as well. The resulting curve is `29x^2 + 2x + 5398021`, meaning the secret is `5398021`.

#### Step 4
If you look at the length of the given `flags.txt` file, and the prompt, you should be able to figure out that this number corresponds to the index of the flag in the file. If you look on line `5398021` you get the flag: `utflag{wOq0}`.
