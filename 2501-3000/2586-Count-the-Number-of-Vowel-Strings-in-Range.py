class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels = {"a", "e", "i", "o", "u"}
        countWords = 0
        
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                countWords += 1
        
        return countWords