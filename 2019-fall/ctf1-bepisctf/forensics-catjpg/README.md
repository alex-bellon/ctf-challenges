# cat.jpg
* **Event:** BepisCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:**
* **(Optional) Tools Required / Used:** [exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/)
​

## Steps​
#### Step 1
The prompt mentions something about comments, which is meant to lead you to [EXIF](https://en.wikipedia.org/wiki/Exif) data comments. EXIF metadata often includes things like when the photo was taken, sometimes information about the camera, etc., etc. It also can include comments, which in this case is where the flag is hidden.

#### Step 2
You can look at the properties of the file in a file explorer to see the EXIF metadata, but you can also use a tool like [exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/) to see it on any operating system. You'll find the flag in the comments field: `utflag{mfw_i_@ctu@lly_hav3_t0_writ3_@_pr0bl3m}`.
