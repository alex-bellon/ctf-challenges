# Sandwiched
* **Event:** stonksCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**


## Steps
#### Step 1
When you open up the file, you will see that it's just an (almost) empty PDF file, so that's a dead end. If you start to look at the actual bytes of a file with a tool like [`binwalk`](https://github.com/ReFirmLabs/binwalk) or [`xxd`](https://linux.die.net/man/1/xxd), you will see that there are actually a few files in this thing: A PDF, what seems to be a PNG, and another PDF. 

#### Step 2
If you extract the PNG part of the file and try to open it, you will only get the top half of an image. Luckily, further investigation of the file shows us there's actually more PNG data further down! You can tell which parts of what file start where using the following hex sequences:

- PDF Header: `25 50 44 46 2D`
- PDF Footer: `25 25 45 4F 46`
- PNG Header: `89 50 4E 47 0D 0A 1A 0A`
- PNG Footer: `49 45 4E 44 AE 42 60 82`

Once you have isolated the two chunks of PNG data, you can combine them with a tool like `cat` into a full PNG and then open it to get the flag: `utflag{deepfingvalue}`
