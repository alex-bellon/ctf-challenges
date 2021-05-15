# Bookkeeping
* **Event:** flagCTF
* **Problem Type:** Misc
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
When you connect to the service, you are asked to validate 1000 ISBN-10 numbers. If you do some searching around, you'll find that you can validate whether or not an ISBN-10 number is legit by using the [check digit](https://en.wikipedia.org/wiki/International_Standard_Book_Number#Check_digits).

#### Step 2
Since you need to verify 1000 of these codes, it's best to set up a script that will receive each number and verify it automatically. You'll either have to implement the algorithm yourself (which isn't too hard) or use something that already exists. Once you get 1000 correct, you'll get the flag: `utflag{what_does_this_have_to_do_with_flags}`
