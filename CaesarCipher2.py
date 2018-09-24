from collections import Counter
import string

letters = string.ascii_lowercase
specChars = string.punctuation

# Problem 2
def findKey(cipher):
    mostCommonIndex = 4

    distDict = findLetterDist(cipher)

    commLetter = sorted(distDict, key = distDict.get, reverse = True)

    key = letters.find(commLetter[0].lower()) - mostCommonIndex
    return key

def findLetterDist(cipher):
    distDict = {}
    for letter in cipher:
        if letter in specChars or letter == ' ':
            continue
        if letter not in distDict:
            distDict[letter] = 1
        else:
            distDict[letter] += 1
    return distDict

def main():
    # Problem 2
    f_input = input('File Name: ')

    text = open(f_input, 'r').read().lower().strip()
    outText = open('decrypted_caesar.txt', 'w')
    
    textLen = int(len(text))

    with open(f_input, 'r') as f:
        distDict = Counter(letter for line in f
                          for letter in line.lower()
                          if letter in letters)

    print(distDict)
    
    key = findKey(text)
    
    print("Key: " + str(key))

    # Problem 3
    plain = ""

    for i in range(textLen):
        if text[i].isalpha():
            i = letters.find(text[i])
            j = (i - key) % 26
        else:
            plain += text[i]
            continue
        decrypted = letters[j]
        plain += decrypted

    print(plain)

    with outText as f:
        f.write(plain)
    
main()
