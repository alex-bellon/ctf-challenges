from PIL import Image

def encode():
    image = str(input('What image do you want to use as cover? ') )
    plain = str(input('What\'s the message you want to embed? '))
    message = list()
    for letter in plain:
        message.append(ord(letter))
    
    original = Image.open(image)
    channels = original.split()
    r = channels[0]
    g = channels[1]
    b = channels[2]
    x_ = original.size[0]
    y_ = original.size[1]

    encoded = Image.new('RGB', original.size)
    output = encoded.load()

    i = 0
    for x in range(x_):
        for y in range(y_):
            rPixel = r.getpixel((x, y))
            gPixel = g.getpixel((x, y))
            bPixel = b.getpixel((x, y))
            if (i < len(message)):
                if (i % 3 == 0):
                    rPixel = message[i]
                elif (i % 3 == 1):
                    gPixel = message[i]
                elif (i % 3 == 2):
                    bPixel = message[i]
            output[x, y] = (rPixel, gPixel, bPixel)
            i += 1

    encoded.save("secret.png")

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

def main():
    choice = input('Do you want to encode or decode? [e/d] ')
    if str(choice).lower() == 'e':
        encode()
    if str(choice).lower() == 'd':
        decode()

main()
