class Solution(object):
    def kInversePairs(self, n, k):
        p = 10**9 + 7
        currentCount = [1] + [0] * k

        for i in range(2, n+1):
            nextCount = [1] + [0] * k
            for j in range(1, k + 1): 
                nextCount[j] += nextCount[j-1] + currentCount[j]

                if j >= i:
                    nextCount[j] -= currentCount[j-i]
            currentCount = nextCount

        return currentCount[k] % p