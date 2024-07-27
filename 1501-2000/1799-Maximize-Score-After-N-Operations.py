class Solution(object):
    def maxScore(self, nums):
        n = len(nums) // 2
        
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        gcds = defaultdict(int)
        
        for i in range(2*n):
            for j in range(i+1, 2*n):
                gcds[(nums[i], nums[j])] = gcd(nums[i], nums[j])
        
        maxVals = defaultdict(int)
        
        def maxVal(i, mask):
            if i > n:
                return 0
            
            if (i, mask) in maxVals:
                return maxVals[(i, mask)]
            
            res = 0
            for j in range(2*n):
                for k in range(j + 1, 2*n):
                    new_mask = (1 << j) + (1 << k)
                    if not mask & new_mask:
                        res = max(res, i * gcds[(nums[j], nums[k])] + maxVal(i + 1, mask + new_mask))
            
            maxVals[(i, mask)] = res
            return res
        
        return maxVal(1, 0)