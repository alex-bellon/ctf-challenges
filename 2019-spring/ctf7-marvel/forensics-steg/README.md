# RGB
* **Event:** MarvelCTF
* **Problem Type:** Forensics
* **Point Value / Difficulty:** Hard
* **(Optional) Tools Required / Used:**

## Steps​
#### Step 1
This is a steganography challenge with a little twist. It is similar to [least significat-bit steganography](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit_in_digital_steganography), but instead of using every bit, it alternates between embedding information only in the Red, Green or Blue byte (hence the title). 

#### Step 2
You can write a Python script to retrieve the flag that looks something like this:
```python
def decode():
    image = str(input('What image is the message hidden in? ') )
    length = int(input('How many bytes do you want to check? '))
    encoded = Image.open(image)
    channels = encoded.split()
    r = channels[0]
    g = channels[1]
    b = channels[2]
    x_ = encoded.size[0]
    y_ = encoded.size[1]

    decoded = ''

    i = 0
    for x in range(x_):
        for y in range(y_):
            rPixel = r.getpixel((x, y))
            gPixel = g.getpixel((x, y))
            bPixel = b.getpixel((x, y))
            if (i < length):
                if (i % 3 == 0):
                    decoded += chr(rPixel)
                elif (i % 3 == 1):
                    decoded += chr(gPixel)
                elif (i % 3 == 2):
                    decoded += chr(bPixel)
            i += 1
    
    print(decoded)
```
to get the flag: `utflag{0n3_byt3_at_a_t1m3}`.
