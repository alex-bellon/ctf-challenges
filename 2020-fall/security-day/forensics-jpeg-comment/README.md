# True Hacker
* **Event:** Security Day 2020
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The hint in the prompt about "comments" is referring to the comment metdata field that JPEGs (and other file formats) have. 

#### Step 2
In order to see this comment, you can right-click on the image and view the Properties (or whatever it's called on your system) of the image. You can also use the terminal command `strings true-hacker-form.jpg` to get all the strings in a file. Both will lead you to the flag" `utflag{k33p_y0ur_c0mm3nts_t0_y0urs3lf}`. 
