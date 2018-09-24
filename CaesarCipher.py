import collections
import string

MAX_KEY = 26
letters = string.ascii_lowercase
symbols = string.punctuation

while True:
    key = int(input("Please enter a key (1-26): "))
    if key > MAX_KEY:
        print("Error: Number must be between 1 and 26. Please try again.")
        continue
    else:
        break

inFile = str(input('Please enter an input file name: '))
outFile = str(input('Please enter an output file name: '))

inText = open(inFile, 'r').read().lower().strip()
outText = open(outFile, 'w')

inTextLen = int(len(inText))
cipher = ''

for i in range(inTextLen):
    if inText[i].isalpha():
        i = letters.find(inText[i])
        j = (i + key) % MAX_KEY
    else:
        cipher += inText[i]
        continue
    coded = letters[j]
    cipher += coded

with outText as f:
    f.write(cipher)
