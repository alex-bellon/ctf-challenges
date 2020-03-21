# GIFAR 
* **Event:** ForniteCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
If you open `epic-floss-meme.jpg`, you'll see that the flag isn't there. If you use a tool like `binwalk` on the file though, you'll see that there is a ZIP file embedded in the image. 

#### Step 2
You could try to file carve the ZIP out, but because of the way ZIP has its file headers/trailers set up, you can also just run `unzip epic-floss-meme.jpg`. This will give you a file with the flag: `utflag{fl0ss_f0r_100_fr33_p01nts}`.

