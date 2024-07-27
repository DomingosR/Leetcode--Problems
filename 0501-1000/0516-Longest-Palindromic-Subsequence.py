class Solution(object):
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0

        n = len(s)
        s1 = s[::-1]
        currentMaxLen = [0] * (n+1)

        for i in range(n):
            nextMaxLen = [0] * (n+1)
            for j in range(1, n+1):
                if s[i] == s1[j-1]:
                    nextMaxLen[j] = currentMaxLen[j-1] + 1
                else:
                    nextMaxLen[j] = max(nextMaxLen[j-1], currentMaxLen[j])
            currentMaxLen = nextMaxLen

        return currentMaxLen[-1]
