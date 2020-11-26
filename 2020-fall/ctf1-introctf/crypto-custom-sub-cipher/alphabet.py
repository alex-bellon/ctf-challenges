alphabet = {
  'a': '🤠',
  'f': '👽',
  'g': '👾',
  'l': '👀',
  't': '🎩',
  'u': '🦈',
}

plain = "utflag{fatal_alfalfa_fluff}"
#plain = input("Enter flag: ")
result = ""

for letter in plain:
    if letter in alphabet:
        result += alphabet[letter]
    else:
        result += letter

print(result)
