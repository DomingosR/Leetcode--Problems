class Solution(object):
    def putMarbles(self, weights, k):
        n = len(weights)
        pairSums = [sum(weights[i:i+2]) for i in range(n-1)]
        pairSums.sort()
        
        return sum(pairSums[n-k:]) - sum(pairSums[:k-1])