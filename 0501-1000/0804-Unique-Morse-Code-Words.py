from collections import defaultdict

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morseAlphabet = [".-","-...","-.-.","-..",".","..-.","--.", \
                         "....","..",".---","-.-",".-..","--","-.","---",\
                         ".--.","--.-",".-.","...","-","..-","...-",".--",\
                         "-..-","-.--","--.."]
        encodingDict = {}

        for word in words:
            encoding = ""
            for letter in word:
                index = ord(letter) - ord("a")
                encoding += morseAlphabet[index]
            encodingDict[encoding] = encodingDict.get(encoding, 0) + 1

        return len(encodingDict)
