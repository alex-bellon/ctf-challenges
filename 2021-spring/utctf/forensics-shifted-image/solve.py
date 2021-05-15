from PIL import Image
import numpy

image = Image.open('SHIFT.png')
pixels = list(image.getdata())
w, h = image.size

# split pixels by row
pixels = [pixels[i * w : (i + 1) * w] for i in range(h)]

result = []

shift = 0
for row in pixels:
    # get two halves of row
    left = row[:w - shift]
    right = row[w - shift:]

    # flip the two halves (this unshifts them)
    new_row = right + left

    # increase shift and wrap around row length
    shift = (shift + 6) % w
    result.append(new_row)

# save to new image
array = numpy.array(result, dtype=numpy.uint8)
new = Image.fromarray(array)
new.save('flag.png')
