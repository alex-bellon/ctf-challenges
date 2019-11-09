# Zipline
* **Event:** Security Day Fall 2019
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** `unzip` command line tool


## Steps​
#### Step 1
As the title and prompt suggested, this image is more than just a picture, it's also a ZIP archive.

#### Step 2
While you could use `dd` to unzip the specific part of the file that contains the ZIP archive, the simplest way to get the files out is by running `unzip zipline.jpg`. Inside the archive is an image that contains the flag: `utflag{ur_z1p_1s_d0wn}`.

**Why does this work? Read more [here](https://en.wikipedia.org/wiki/Gifar) and [here](https://www.howtogeek.com/119365/how-to-hide-zip-files-inside-a-picture-without-any-extra-software/).**
