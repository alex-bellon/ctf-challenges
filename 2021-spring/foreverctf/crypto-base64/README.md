# All Your Base Are Belong To Us
* **Event:** ForeverCTF
* **Problem Type:** Crypto
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
If you look into ciphers/encoding schemes that use `=`s at the end (or if you follow the information from the hints), you should find [Base64](https://en.wikipedia.org/wiki/Base64), an encoding scheme that uses 64 characters to represent data, and usually pads the end of the encoded data with one or two `=`s.

#### Step 2
You can use an online decoder like [this](https://www.base64decode.org/) or the terminal command `echo dXRmbGFne2NvdmVyZWRfYWxsXzY0X2Jhc2VzfQo= | base64 -d` (send the encoded string to the `base64` program in decode mode) to recover the flag: `utflag{covered_all_64_bases}`.
