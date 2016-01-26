import sys
import os.path

def encryptCharacter(character):
    encryptedCharacter = ord(character)
    encryptedCharacter = encryptedCharacter << 1
    encryptedCharacter = chr(encryptedCharacter)
    return encryptedCharacter

def decryptCharacter(character):
    decryptedCharacter = ord(character)
    decryptedCharacter = decryptedCharacter >> 1
    decryptedCharacter = chr(decryptedCharacter)
    return decryptedCharacter

arg = sys.argv[1]
if not os.path.exists(arg):
    sys.exit("File doesn't exists")

f = open(arg)

encryptedString = ''
for line in f:
    print line
    for character in line:
        encryptedString += encryptCharacter(character)
print encryptedString

f.seek(0)
decryptedString = ''
for line in f:
    print line
    for character in line:
        print character
        decryptedString += decryptCharacter(character)

print decryptedString
