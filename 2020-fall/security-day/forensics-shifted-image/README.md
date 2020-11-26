# SHIFT
* **Event:** Security Day 2020
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Medium
* **(Optional) Tools Required / Used:**

## Steps
#### Step 1
When you open the image, you should be able to tell that each row of the image has been gradually shifted over further and further. Pixels wrap back around to the front of the row if they go past the width of the image.

#### Step 2
In order to solve this, you'll have to write a script to shift all of the rows back to their original position. Here's one that I wrote in Python:

```python
from PIL import Image
import numpy

image = Image.open('shift.png')
pixels = list(image.getdata())
w, h = image.size

# split pixels by row
pixels = [pixels[i * w : (i + 1) * w] for i in range(h)]

new_pixels = []

shift = 0
for row in pixels:
    # get two halves of row
    left = row[:w - shift]
    right = row[w - shift:]

    # flip the two halves (this unshifts them)
    new_row = right + left

    # increase shift and wrap around row length
    shift = (shift + 5) % w
    result.append(new_row)

# save to new image
array = numpy.array(result, dtype=numpy.uint8)
new = Image.fromarray(array)
new.save('out.png')
```

You would have to guess the shift increment by trial and error, but even if you're off by plus or minus 2 pixels, the flag should still be readable.
