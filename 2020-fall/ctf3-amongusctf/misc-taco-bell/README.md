# Live Mas
* **Event:** AmongUsCTF
* **Problem Type:** Misc
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
When you connect to the service, you are asked to validate 1000 Taco Bell survey codes. If you do some searching around, you'll find that you can validate whether or not a Taco Bell survey code is legit by using the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

#### Step 2
Since you need to verify 1000 of these codes, it's best to set up a script that will receive each number and verify it automatically. You'll either have to implement the algorithm yourself (which isn't too hard) or use something that already exists. Once you get 1000 correct, you'll get the flag: `utflag{blue_was_not_the_impostor}`
