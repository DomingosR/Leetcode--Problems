class Solution(object):
    def numTilings(self, n):
        p = 10**9 + 7
        if n==1:
            return 1

        countTilings = [0] * (2*n + 1)
        countTilings[2] = 1
        countTilings[3] = 1
        countTilings[4] = 2

        for i in range(5, 2*n + 1):
            if i % 2 == 0:
                countTilings[i] = countTilings[i-2] + countTilings[i-4] + 2*countTilings[i-3]
            else:
                countTilings[i] = countTilings[i-2] + countTilings[i-3]
            countTilings[i] = countTilings[i] % p
        
        return countTilings[-1]