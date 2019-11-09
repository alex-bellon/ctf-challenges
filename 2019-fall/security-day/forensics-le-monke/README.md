# Le Monke
* **Event:** Security Day Fall 2019
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**


## Steps​
#### Step 1
There wasn't really any information given in the prompt, but if you open up the image, there is a strange watermark in the top right corner.

#### Step 2
The mark in the upper right corner is a box that has rectangles inside of it. If you look closely, you'll see that the mark is 8 rectangles high, which is the same amount of numbers that it takes to represent letters in binary. If you interpret each column as a letter, each rectangle in the column as a 1, and each gap/space in the column as a 0, you can decode the mark into this binary string: `01110101 01110100 01100110 01101100 01100001 01100111 01111011 01110101 01101000 01011111 00110000 01101000 01011111 01110011 01110100 00110001 01101110 01101011 01111001 01111001 01111001 01111001 01111001 01111101`. Convert those binary strings to ASCII letters and you get `utflag{uh_0h_st1nkyyyyy}`.
