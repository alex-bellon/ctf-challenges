# OTP
* **Event:** ForeverCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**
​
## Steps​
#### Step 1
From the prompt and problem title, you should hopefully figure out that this problem is exploiting key reuse in a [One Time Pad](https://en.wikipedia.org/wiki/One-time_pad) scheme. As the name of the scheme suggests, pads/keys should only be used once or else you can recover the key, for reasons demonstrated in [this article](https://samwho.dev/blog/toying-with-cryptography-crib-dragging/).

#### Step 2
You can then use an online tool like [this](https://toolbox.lotusfa.com/crib_drag/) (or any other crib dragging tool) to guess for words in the plaintexts. Since the prompt mentions that they are arguing about ice cream flavors, you can eventually guess common related words/phrases that lead to these two plaintext messages:

```
THE BEST ICE CREAM FLAVOR IS MINT CHOCOLATE
NO THE BEST ICE CREAM FLAVOR IS STRAWBERRY!
```

#### Step 3
From there, you can get the key (which is the flag) by XORing the plaintext with the correct ciphertext (you might have to do a little trial and error here). Then you can get the key (and the flag) `utflag{what_is_crib_dragging_anyways}`.
