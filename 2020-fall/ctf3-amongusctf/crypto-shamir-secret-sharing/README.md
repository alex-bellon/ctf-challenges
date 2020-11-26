# Sharing Secrets
* **Event:** AmongUsCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
From the title and name of the character, you should be able to find out that this problem has to do with [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing). There are enough shares here to get the secret, so we can just plug and chug.

#### Step 2
Using the same math shown in this [walkthrough](https://medium.com/@apogiatzis/shamirs-secret-sharing-a-numeric-example-walkthrough-a59b288c34c4) (the math works, I just don't want to copy it all here), you can calculate that the shared secret is 3957230. Thus the flag is `utflag{3957230}`.
