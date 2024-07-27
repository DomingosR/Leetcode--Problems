class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowedLetters = set(allowed)
        allowedWords = [word for word in words if set(word).issubset(allowedLetters)]
        return len(allowedWords)