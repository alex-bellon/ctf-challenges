# Magic
* **Event:** ForeverCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**
​
## Steps​
#### Step 1
If you try to open up this image, you won't be able to because the file is corrupted. If you use a tool like `xxd`, you will see that something is wrong with bytes of the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures) -- they're all 0s instead of what they should be for a PNG: `89 50 4E 47`. Since computers use these file signatures to determine what to do with a file, the computer has no idea what to do in this situation since all 0s isn't the beginning of a valid filetype (at least an image filetype).

#### Step 2
If you edit the hex of the file (using something like [`bless`](https://github.com/afrantzis/bless)) and restore the first four bytes back to `89 50 4E 47`, you should be able to open the file again and see the flag: `utflag{dont_lose_your_headers}`.
