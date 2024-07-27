class Solution(object):
    def numDistinct(self, s, t):
        lenS = len(s)
        lenT = len(t)
        
        numSubseq = [[0] * lenT for _ in range(lenS)]
        if s[0] == t[0]:
            numSubseq[0][0] = 1
        
        for i in range(1, lenS):
            numSubseq[i][0] = numSubseq[i-1][0] + (s[i] == t[0])
        
        for j in range(1, lenT):
            for i in range(1, lenS):
                numSubseq[i][j] = numSubseq[i-1][j] + numSubseq[i-1][j-1] * (s[i] == t[j])

        return numSubseq[-1][-1]