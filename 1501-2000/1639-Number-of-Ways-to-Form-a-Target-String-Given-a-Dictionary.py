class Solution(object):
    def numWays(self, words, target):
        p = 10**9 + 7
        m = len(target)
        n = len(words[0])

        numWays = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m-1, -1, -1):
            if i == m-1:
                for j in range(i+n-m, i-1, -1):
                    numWays[i][j] = sum([1 for word in words if word[j] == target[i]])
            else:
                partial = 0
                for j in range(i+n-m, i-1, -1):
                    partial += numWays[i+1][j+1]
                    numWays[i][j] = partial * sum([1 for word in words if word[j] == target[i]])
        
        return sum(numWays[0]) % p