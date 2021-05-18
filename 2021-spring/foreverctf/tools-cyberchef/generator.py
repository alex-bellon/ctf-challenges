# binary > base64 > caesar > final
import base64, string

binaryFile = open('binary.txt', 'w')
base64File = open('base64.txt', 'w')
caesarFile = open('caesar.txt', 'w')
finalFile = open('final.txt', 'w')

flag = input('Enter flag (without utflag{ }): ')
finalContent = 'utflag{' + str(flag) + '}'


#### CAESAR

shift = 10
caesar = ''
for char in finalContent:
    if char.isupper():
        caesar = caesar + chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
        caesar = caesar + chr((ord(char) + shift - 97) % 26 + 97)
    else:
        caesar = caesar + char

caesarContent = caesar


##### BASE64

base = base64.b64encode(bytes(caesarContent, 'utf-8')).decode('ascii')
base64Content = base


##### BINARY

binaryContent = ' '.join(format(ord(i),'b').zfill(8) for i in base64Content)

#### WRITE TO FILES

binaryFile.write(binaryContent + '\n')
base64File.write(base64Content + '\n')
caesarFile.write(caesarContent + '\n')
finalFile.write(finalContent + '\n')
