class Solution(object):
    def numberOfArrays(self, s, k):
        n = len(s)
        numWays = [0] * (n+1)
        numWays[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] != "0":
                j = 1
                while int(s[i:i+j]) <= k and (i + j <= n):
                    numWays[i] += numWays[i+j] % (10**9 + 7)
                    j += 1
                numWays[i] = numWays[i] % (10**9 + 7)

        return numWays[0]
