# binary > base64 > caesar > substituted > final
import base64, string

binaryFile = open('binary.txt', 'w')
base64File = open('base64.txt', 'w')
caesarFile = open('caesar.txt', 'w')
substitutedFile = open('subsituted.txt', 'w')
finalFile = open('final.txt', 'w')

flag = input('Enter flag: ')
finalContent = 'congratulations! you have finished the beginner cryptography challenge. here is a flag for all your hard efforts: utflag{' + str(flag) + '}. you will find that a lot of cryptography is just building off this sort of basic knowledge, and it really is not so bad after all. hope you enjoyed the challenge!'


#### SUBSTITUTION CIPHER

subs = {'a': 'i', 'c': 'h', 'b': 'p', 'e': 'a', 'd': 'u', 'g': 'd', 'f': 's', 'i': 'j', 'h': 'y', 'k': 'r', 'j': 'f', 'm': 'e', 'l': 'o', 'o': 'w', 'n': 'x', 'q': 'm', 'p': 'b', 's': 'k', 'r': 'n', 'u': 'v', 't': 't', 'w': 'l', 'v': 'q', 'y': 'g', 'x': 'c', 'z': 'z'}
substitution = ''
for char in finalContent:
    if ord(char) >= 97 and ord(char) <= 122:
        substitution += subs[char]
    else:
        substitution += char

substitutedContent = 'alright, you\'re almost there! Now for the final (and maybe the hardest...) part: a substitution cipher. In the following text, I\'ve taken my message and replaced every alphabetic character with a correspondence to a different character - known as a substitution cipher. Can you find the final flag? hint: We know that the flag is going to be of the format utflag{...} - which means that if you see that pattern, you know what the correspondences for u, t, f, l a, and g are. You can probably work out the remaining characters by replacing them and inferring common words in the English language. Another great method is to use frequency analysis: we know that \'e\' shows up most often in the alphabet, so that\'s probably the most common character in the text, followed by \'t\', and so on. Once you know a few characters, you can infer the rest of the words based on common words that show up in the English language.\n' + substitution


#### CAESAR

shift = 10
caesar = ''
for char in substitutedContent:
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
substitutedFile.write(substitutedContent + '\n')
finalFile.write(finalContent + '\n')
