# Inconspicuous Image
* **Event:** flagCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:** `unzip` command line tool


## Steps
#### Step 1
As the prompt suggested, this image is more than just a picture, it's also a ZIP archive. You can figure this out by using a tool like `binwalk` and seeing the embedded ZIP, or `xxd` and noticing the ZIP file header/footer.

#### Step 2
While you could use `dd` to unzip the specific part of the file that contains the ZIP archive, the simplest way to get the files out is by running `unzip flag.jpg`. Inside the archive is an image that contains the flag: `utflag{flagception}`.

**Why does this work? Read more [here](https://en.wikipedia.org/wiki/Gifar) and [here](https://www.howtogeek.com/119365/how-to-hide-zip-files-inside-a-picture-without-any-extra-software/).**
