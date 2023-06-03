# TextFileEncryptor
Basic CLI-Based text encryptor<br>
I created this in 2021 for the AP Computer Science Principles project

# How it works
Insert text into file.txt to be encrypted (the message itself is encrypted within the file)<br>
Each supported character has a 3 number key value. The new encrypted message finds the 3 number key, and adds a random number.<br>
To get the private key, the random number is multiplied by a set value within main.py called bigNumber<br>
To decrypt, the program takes the private key, extracts the random number, and reverses the encryption method<br>

# Limitations
This program is not meant to be used as a legitimate encrypting method, as it is relatively easy to decipher by hand, although it may take a while<br>
Program also triples the size of the text file, so it can only work well with smaller messages<br>
