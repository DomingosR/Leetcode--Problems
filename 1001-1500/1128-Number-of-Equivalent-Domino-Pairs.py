class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        numCounter = Counter()
        
        for m, n in dominoes:
            value = 10 * max(m, n) + min(m, n)
            numCounter[value] += 1
            
        return sum([val * (val - 1) // 2 for val in numCounter.values()])