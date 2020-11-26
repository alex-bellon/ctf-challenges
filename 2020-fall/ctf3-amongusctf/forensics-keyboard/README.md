# Click Clack Moo
* **Event:** AmongUsCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Easy
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
You're given Base64 encoded data, which you can decode in the terminal or using a website like [this](https://www.base64decode.org/). You can tell the data is Base64 encoded from the characteristic "==" padding at the end. 

#### Step 2
When you decode the Base64, you'll get this:

```
var events = [ 85, 84, 70, 76, 74, 52, 99, 8, 8, 8, 65, 71, 16, 219, 72, 85, 78, 84, 189, 65, 78, 68, 189, 80, 69, 77, 8, 67, 75, 16, 221]
```

Using some combination of the hint that this is JavaScript, the name of the array, and the title of the problem, you should be able to figure out that these codes are [JavaScript Event KeyCodes](https://keycode.info). You can write a script to convert them back, or do it by hand, but eventually you should get a list of keys that were pressed. Once you remove the extraneous letters (the ones followed by backspaces), you should get the flag: `utflag{hunt-and-peck}`
