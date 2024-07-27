class Solution(object):
    def minEatingSpeed(self, piles, h):
        n = len(piles)
        if n > h:
            return -1
        
        minK = 1
        maxK = max(piles)
        
        while minK < maxK:
            trialK = (minK + maxK) // 2
            numHours = sum(math.ceil(1.0 * pile/trialK) for pile in piles)
            if numHours > h:
                minK = trialK + 1
            else:
                maxK = trialK
        
        return minK