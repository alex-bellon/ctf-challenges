# OTP
* **Event:** UTC-CTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:** [Crib Drag Calculator](https://toolbox.lotusfa.com/crib_drag/)

## Steps
#### Step 1
The title of the challenge and the mention of key reuse in the prompt should lead you to something like [this article](https://incoherency.co.uk/blog/stories/otp-key-reuse.html), explaining how key reuse can allow you to recover both plaintexts and the key. 

#### Step 2
In order to do this, you need to use a technique called crib-dragging, where you guess likley plaintexts. If you use and online tool like [Crib Drag Calculator](https://toolbox.lotusfa.com/crib_drag/), and use the theme in the hint (the best season), you will find the two plaintexts:

```
MY FAVORITE SEASON IS TOTALLY THE SUMMER
NO WAY THE BEST SEASON IS TOTALLY SPRING
```

If you XOR one of these messages with their ciphertexts, you will get the key (which is also the flag!): `utc{drag_those_cribs}`
