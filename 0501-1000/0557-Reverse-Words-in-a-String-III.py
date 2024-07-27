class Solution(object):
    def reverseWords(self, s):
        indWords = s.split()
        reversedWords = [word[::-1] for word in indWords]
        return " ".join(reversedWords)