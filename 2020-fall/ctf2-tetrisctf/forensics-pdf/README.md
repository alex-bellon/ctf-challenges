# Wumbo
* **Event:** TetrisCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
The prompt mentions that the PDF file got cut off at the top (and you can see that if you open it in Chrome or another PDF reader). If you do some searching, you'll find that there are different types of [boundary boxes](https://www.prepressure.com/pdf/basics/page-boxes) for PDFs that change how they are rendered and displayed.

#### Step 2
If you open the contents of the PDF in a text editor, you will see that there is a CropBox included in the PDF, which is cutting off the full page:

```
<i< /Contents 10 0 R /MediaBox [ 0 0 612 792 ] /CropBox [ 0 0 612 600 ] ...
```

You can then delete that CropBox

```
<< /Contents 10 0 R /MediaBox [ 0 0 612 792 ] ...
```
and save the file to see the whole original PDF that includes the flag: `utflag{whats_a_cropbox}`

