# As(key) Art
* **Event:** ThankfulCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:**
​
## Steps​
#### Step 1
If you read the prompt, it mentions "SSH Identicons". A quick search for the term will bring up a [few](https://dev.to/krofdrakula/improving-security-by-drawing-identicons-for-ssh-keys-24mc) [articles](https://tylercipriani.com/blog/2017/09/26/ssh-key-fingerprints-identicons-and-ascii-art/) that explain how these identicons are generated. They both reference [this whitepaper](http://www.dirk-loss.de/sshvis/drunken_bishop.pdf), which describes the algorithm in detail. Normally, you should not be able to reverse engineer SSH identicons, but I handcrafted (*chef's kiss*) this key so that it is possible to reverse engineer it.

#### Step 2
If you trace the steps of the "drunken bishop" backwards, you can get the corresponding binary representation of the SSH fingerprint (in a bit of a mixed order). Once you order it properly and convert it to hex, you should get the flag: `55fe8002`
