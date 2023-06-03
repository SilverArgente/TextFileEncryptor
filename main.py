# Text File Encryptor
# HOW TO OPERATE: Put text into file.txt, and then run program

# Imports
import os
import random
from encoder import *
from decoder import *

# Gets size of files, important for getting the amount of characters in a file (1 character = 1 byte)
def getSize(filename):
    st = os.stat(filename)
    return st.st_size


bigNumber = 12345

fileLen = getSize("file.txt")

# New encrypted array
encryptedChars = [None] * fileLen
decryptedChars = [None] * fileLen

prompt = input("Would you like to encrypt or decrypt file? (Enter e or d): ")

if (prompt == 'd'):
    print("You have chosen to decrypt your file.")
    passW = input("Please enter file password: ")

    num = int(passW) / bigNumber
    f = open("file.txt", "r")

    # Appends entire file into one variable
    txtFile = f.read()

    # Initizalize character array with length of file
    fileChars = [None] * fileLen

    # Loops through the file's text and appends each character to the array
    for i in range(fileLen):
        fileChars[i] = txtFile[i:i + 1]

    f.close()
    f = open("file.txt", "w")
    f.truncate()

    c = 0
    j = 0
    decrypted = False

    while (decrypted == False):
        decryptedChars[c] = fileChars[j] + fileChars[j + 1] + fileChars[j + 2]
        c += 1
        j += 3
        if (c == fileLen / 3):
            decrypted = True

    for i in range(int(fileLen / 3)):
        temp = decryptedChars[i]
        decryptedChars[i] = int(temp) - int(num)
        decryptedChars[i] = returnDecodedChar(decryptedChars[i])
        f.write(str(decryptedChars[i]))

    f.close()

else:
    print("You have chosen to encrypt your file.")

    # Opens the text file
    f = open("file.txt", "r")

    # Appends entire file into one variable
    txtFile = f.read()

    # Initizalize character array with length of file
    fileChars = [None] * fileLen

    # Loops through the file's text and appends each character to the array
    for i in range(fileLen):
        fileChars[i] = txtFile[i:i + 1]

    f.close()
    f = open("file.txt", "w")
    f.truncate()

    f.close()

    f = open("file.txt", "a")

    # Loops through file's characters, encodes each character and sends it to new encrypted character array
    for i in range(0, len(encryptedChars)):
        tempChar = fileChars[i]
        tempEncodedChar = returnEncodedChar(tempChar)
        encryptedChars[i] = tempEncodedChar

    # Gets random number for key
    keyRandNum = random.randint(1, 99)

    print("Your private key is " + str(keyRandNum * bigNumber))

    # Adds key to each value in encrypted array
    for i in range(0, len(encryptedChars)):
        encryptedChars[i] += keyRandNum
        f.write(str(encryptedChars[i]))

    f.close()

    print("File has been successfully encrypted.")