class Solution(object):
    def numOfArrays(self, n, m, k):
        maxVal = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
        p = 10**9 + 7

        for j in range(m+1):
            maxVal[1][j][1] = 1

        for s in range(1, n+1):
            for t in range(1, m+1):
                for u in range(1, k+1):
                    auxVal = 0
                    for v in range(1, t):
                        auxVal += maxVal[s-1][v][u-1] % p
                    auxVal += t * maxVal[s-1][t][u] % p
                    maxVal[s][t][u] += auxVal
                    maxVal[s][t][u] = maxVal[s][t][u] % p

        returnVal = 0
        for t in range(1, m+1):
            returnVal += maxVal[n][t][k]
        return returnVal % p
