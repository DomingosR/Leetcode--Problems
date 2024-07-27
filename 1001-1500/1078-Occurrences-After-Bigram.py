class Solution(object):
    def findOcurrences(self, text, first, second):
        words = text.split(" ")
        n = len(words)
        followingWords = []

        for i in range(n-2):
            if words[i] == first and words[i+1] == second:
                followingWords.append(words[i+2])

        return followingWords
