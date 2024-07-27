class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split(" ")
        foundIndex = -1
        numChars = len(searchWord)
        numWords = len(words)
        
        for i in range(len(words)):
            if words[i][:numChars] == searchWord:
                foundIndex = i+1
                break
        
        return foundIndex