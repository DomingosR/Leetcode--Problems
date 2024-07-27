class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        if not (text1 and text2):
            return 0

        if len(text1) > len(text2):
            auxText = text1
            text1 = text2
            text2 = auxText

        m = len(text1)
        n = len(text2)

        currentMaxLen = [0] * (n+1)
        for i in range(m):
            nextMaxLen = [0] * (n+1)
            for j in range(1, n+1):
                if text1[i] == text2[j-1]:
                    nextMaxLen[j] = currentMaxLen[j-1] + 1
                else:
                    nextMaxLen[j] = max(nextMaxLen[j-1], currentMaxLen[j])
            currentMaxLen = nextMaxLen

        return currentMaxLen[-1]