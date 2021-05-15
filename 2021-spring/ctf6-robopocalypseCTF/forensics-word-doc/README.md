# Documented
* **Event:** RobopocalypseCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The prompt mentions that we're looking for an image, but you are only given a `.docx` file (with no images in it).

#### Step 2
You might already know that you can actually unzip `.docx` archives, but if you don't, then you might also come to this conclusion by running somehting like `binwalk` on the file and seeing compressed image files.

#### Step 3
If you unzip the `.docx`, you can browse through the image files (in `/word/media`) to find the one that contains the flag: `utflag{i_love_microsoft!!!!!}`.

