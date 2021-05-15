# binary > base64 > caesar > substituted > final
import base64, string

binaryFile = open('binary.txt', 'w')
base64File = open('base64.txt', 'w')
caesarFile = open('caesar.txt', 'w')
finalFile = open('final.txt', 'w')


flag = input('Enter flag (without utflag{ }): ')
flagFile = open('flag.txt', 'w')
flagFile.write('utflag{' + flag + '}\n')

finalContent = 'congratulations! you have finished the beginner cryptography challenge. here is a flag for all your hard efforts: utflag{' + str(flag) + '}. you will find that a lot of cryptography is building off this sort of basic knowledge, and it really is not so bad after all. hope you enjoyed the challenge!'

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

caesarContent = 'New challenge! Can you figure out what\'s going on here? It looks like the letters are shifted by some constant. (hint: you might want to start looking up Roman people).\n' + caesar


##### BASE64

#base = base64.b64encode(caesarContent)
#base = caesarContent.encode('ascii').decode('ascii')
base = base64.b64encode(bytes(caesarContent, 'utf-8')).decode('ascii')
base64Content = 'Uh-oh, looks like we have another block of text, with some sort of special encoding. Can you figure out what this encoding is? (hint: if you look carefully, you\'ll notice that there only characters present are A-Z, a-z, 0-9, and sometimes / and +. See if you can find an encoding that looks like this one.)\n' + base


##### BINARY

binaryContent = ' '.join(format(ord(i),'b').zfill(8) for i in base64Content)


#### WRITE TO FILES

binaryFile.write(binaryContent + '\n')
base64File.write(base64Content + '\n')
caesarFile.write(caesarContent + '\n')
finalFile.write(finalContent + '\n')
