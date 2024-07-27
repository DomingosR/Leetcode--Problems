class Solution(object):
    def tallestBillboard(self, rods):
        n = len(rods)
        computedVals = defaultdict(int)
        lowVal = -5001
        
        def maxLen(k, diff):
            if k == n:
                return 0 if diff == 0 else lowVal
            
            if (k, diff) in computedVals:
                return computedVals[(k, diff)]
            
            val1 = rods[k] + maxLen(k+1, diff + rods[k])
            val2 = rods[k] + maxLen(k+1, diff - rods[k])
            val3 = maxLen(k+1, diff)
            optVal = max(val1, val2, val3)
            
            computedVals[(k, diff)] = optVal
            return optVal

        return maxLen(0, 0) // 2 if maxLen(0, 0) > 0 else 0