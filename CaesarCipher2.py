# This is a program to find the key for an encrypted text file, based on the most common letters. This is used to find the key
# for the file, and then use the key to decrypt the file, and then write the decrypted text to an output file.

from collections import Counter # Used to count the number of occurrences of each letter
import string

letters = string.ascii_lowercase # Array to store lowercase letters
specChars = string.punctuation # Special characters

# Find key for decryption
def findKey(cipher):
    mostCommonIndex = 4 # Index of the most common letter 'e'

    distDict = findLetterDist(cipher) # Find the letter distribution for cipher text

    commLetter = sorted(distDict, key = distDict.get, reverse = True) # Sort by most common letter

    key = letters.find(commLetter[0].lower()) - mostCommonIndex # Find key based on most common letter in file
    return key

# Find the letter distribution for the cipher text
def findLetterDist(cipher):
    distDict = {} # Create empty dictionary for cipher distribution
    for letter in cipher: # Read through cipher text
        if letter in specChars or letter == ' ': # Letter is either a special character or a space
            continue
        if letter not in distDict: # Letter is not in distribution dictionary
            distDict[letter] = 1
        else:
            distDict[letter] += 1
    return distDict

# Main method
def main():
    f_input = input('File Name: ') # Prompt user for input file

    text = open(f_input, 'r').read().lower().strip() # Open input file and convert each letter to lowercase
    outText = open('decrypted_caesar.txt', 'w') # Output file where plaintext will be written
    
    textLen = int(len(text)) # Get length of input text file

    # Read through input file, and count the occurrences of each letter
    with open(f_input, 'r') as f:
        distDict = Counter(letter for line in f
                          for letter in line.lower()
                          if letter in letters)

    print(distDict) # Print letter frequencies
    
    key = findKey(text) # Key of text
    
    print("Key: " + str(key)) # Print key
    
    plain = "" # This string will hold the plaintext

    # Read through input file
    for i in range(textLen): 
        if text[i].isalpha(): # Symbol is a letter
            i = letters.find(text[i]) # Map letter in file to letter in array
            j = (i - key) % 26 # Subtract the key from the index of the letter, and use modulo 26
        else: # Symbol is not a letter
            plain += text[i] # Append symbol to plaintext string
            continue
        decrypted = letters[j] # Decrypted letter
        plain += decrypted # Append decrypted letter to plaintext

    print(plain) # Plaintext

    # Write decrypted plaintext to output file
    with outText as f:
        f.write(plain)
    
main() # Call main method
