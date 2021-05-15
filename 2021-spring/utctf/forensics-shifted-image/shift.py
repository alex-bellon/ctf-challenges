from pprint import pprint
from PIL import Image
import numpy

image = Image.open('original.png')

pixels = list(image.getdata())
w, h = image.size
pixels = [pixels[i * w : (i + 1) * w] for i in range(h)]

pprint(pixels)

result = []

shift = 0
for row in pixels:
    left = row[:shift]
    right = row[shift:]
    new_row = right + left
    shift = (shift + 6) % w
    result.append(new_row)

array = numpy.array(result, dtype=numpy.uint8)
new = Image.fromarray(array)
new.save('out.png')
