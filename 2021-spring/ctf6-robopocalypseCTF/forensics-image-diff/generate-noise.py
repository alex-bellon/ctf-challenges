from PIL import Image
import random

pixels = list()

img = Image.new('RGB', (500, 500))

for i in range(500):
    for j in range(500):
        val = random.randint(0, 255)
        pixel = (val, val, val)
        pixels.append(pixel)

img.putdata(pixels)
img.save('noise.png')
