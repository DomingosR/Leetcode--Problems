class Solution(object):
    def minimumAddedCoins(self, coins, target):
        coins.sort()
        
        minUnattainable = 1
        i, n = 0, len(coins)
        coinsAdded = 0
        
        while minUnattainable <= target and i < n:
            coin = coins[i]
            if coin <= minUnattainable:
                minUnattainable += coin
                i += 1
            else:
                coinsAdded += 1
                minUnattainable += minUnattainable
            
        while minUnattainable <= target:
            coinsAdded += 1
            minUnattainable += minUnattainable
            
        return coinsAdded
            