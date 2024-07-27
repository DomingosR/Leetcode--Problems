class Solution(object):
    def firstPalindrome(self, words):
        def isPal(s):
            return s == s[::-1]

        for word in words:
            if isPal(word):
                return word

        return ""
