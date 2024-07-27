class Solution(object):
    def maximumScore(self, a, b, c):
        def maxStones(a, b, c):        
            stones = [a, b, c]
            stones.sort()
            a, b, c = stones
            
            if b == 0:
                return 0
            
            if a == 0:
                return b
            
            return maxStones(a, b-1, c-1) + 1
        
        return maxStones(a, b, c)