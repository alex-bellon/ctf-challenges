# Met A Data
* **Event:** ForeverCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
Between the title and the hints for the problem, you should be able to find out that the flag is somewhere in the [metadata](https://en.wikipedia.org/wiki/Metadata) of the file. JPEGs specifically have something called EXIF metadata that often includes things like when the photo was taken, sometimes information about the camera, etc., etc. It also can include comments, which in this case is where the flag is hidden.

#### Step 2
You can look at the properties of the file in a file explorer to see the EXIF metadata, but you can also use a tool like [this one](https://www.exifdata.com/) to see it on any operating system. Another way you could find the flag is by using the terminal command `strings`, which will look for any strings in any type of file (which in this case would include the flag). Any of these methods should lead you to the flag: `utflag{stringy_thingies}`.
