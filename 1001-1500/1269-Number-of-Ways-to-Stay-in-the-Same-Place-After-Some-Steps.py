class Solution(object):
    def numWays(self, steps, arrLen):
        p = 10 ** 9 + 7
        numWays = [0, 1]

        for i in range(steps):
            numWays[1:] = [sum(numWays[i-1:i+2]) % p for i in range(1, min(arrLen+1, i+3))]

        return numWays[1]
