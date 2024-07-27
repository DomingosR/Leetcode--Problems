class Solution(object):
    def longestPalindrome(self, s):
        longestPal = ""

        def getLongestPal(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        for i in range(len(s)):
            evenPal = getLongestPal(i, i+1)
            oddPal = getLongestPal(i, i)

            longestPal = max(longestPal, evenPal, oddPal, key = len)

        return longestPal
