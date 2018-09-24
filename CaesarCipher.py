# This program uses the Caesar cipher to encrypt a text file, and then write the encrypted message to an output text file.

import collections
import string

MAX_KEY = 26
letters = string.ascii_lowercase # Store all lowercase letters
symbols = string.punctuation # Special characters

# Prompt user for key that must be no higher than 26. If this is the case, re-prompt the user for a key until it is between 1 and 26.
while True:
    key = int(input("Please enter a key (1-26): ")) # Prompt for key
    if key > MAX_KEY: # Check to see if number is higher than 26; if so, prompt user for key until between 1 and 26
        print("Error: Number must be between 1 and 26. Please try again.")
        continue
    else:
        break # Key is between 1 and 26; exit loop

inFile = str(input('Please enter an input file name: ')) # Prompt for input file name
outFile = str(input('Please enter an output file name: ')) # Prompt for output to write encryption to

inText = open(inFile, 'r').read().lower().strip() # Read input file and convert each letter to lowercase
outText = open(outFile, 'w') # Open output file to write encrypted message to

inTextLen = int(len(inText)) # Initialize length of original text
cipher = '' # This string will hold the encrypted message, or cipher text

# Read through input file, and add key to each letter to encrypt it
for i in range(inTextLen):
    if inText[i].isalpha(): # Symbol is a letter
        i = letters.find(inText[i]) # Map each scanned letter
        j = (i + key) % MAX_KEY # Add key to each letter, and use modulo 26
    else: # Symbol is not a letter
        cipher += inText[i] # Add symbol to cipher text
        continue
    coded = letters[j] # Map encrypted letter to letters array
    cipher += coded # Add encrypted letter to cipher text

# Write encrypted message to output file
with outText as f:
    f.write(cipher)
