class Solution(object):
    def countSubstrings(self, s):
        palCount = 0

        def getPalCount(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return count

        for i in range(len(s)):
            palCount += getPalCount(i, i+1) + getPalCount(i, i)
        
        return palCount