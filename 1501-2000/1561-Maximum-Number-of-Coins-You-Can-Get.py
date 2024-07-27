class Solution(object):
    def maxCoins(self, piles):
        n = len(piles) // 3
        piles.sort()
        return sum(piles[n:(3*n+1):2])