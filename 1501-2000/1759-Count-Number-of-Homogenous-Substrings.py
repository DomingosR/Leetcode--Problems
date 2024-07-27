class Solution(object):
    def countHomogenous(self, s):
        numSubstrings, currentChar, i, currentCount, n = 0, "", 0, 0, len(s)
        while i < n:
            if s[i] != currentChar:
                numSubstrings += currentCount * (currentCount + 1) // 2
                currentCount = 1
                currentChar = s[i]
            else:
                currentCount += 1
            i += 1
            if i == n:
                numSubstrings += currentCount * (currentCount + 1) // 2
        return numSubstrings % (10 ** 9 + 7)