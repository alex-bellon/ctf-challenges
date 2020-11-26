# Orange Ricky
* **Event:** TetrisCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** [Steganographic Decoder](https://incoherency.co.uk/image-steganography/#unhide) or [stegsolve](https://github.com/zardus/ctf-tools/tree/master/stegsolve)
​
## Steps​
#### Step 1
The prompt mentions something about hiding an image in another image, as well as 'stego- someting'. If you search up something along the lines of 'stego image hiding' or 'stego forensics', you should stumble upon the actual word I was trying to remember, [steganography](https://en.wikipedia.org/wiki/Steganography).

#### Step 2
While there is software you can download to decode information from steganographic images, the quickest way to extract the data is, as usual, by using an online tool! If you plug in the image to a website like [this](https://incoherency.co.uk/image-steganography/#unhide) and try the different settings for hidden bits, you will be presented with the flag: `utflag{tag_yourself_im_cleveland_z}`. You can also use a commandline tool like `stegsolve`. 
