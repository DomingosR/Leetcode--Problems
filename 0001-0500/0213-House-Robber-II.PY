class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def solveRobber(i, j):
            if j < i:
                return 0
            prevVal = [nums[j], 0]
            for m in range(j-1, i-1, -1):
                currentVal = [prevVal[1] + nums[m], max(prevVal)]
                prevVal = currentVal
            return max(prevVal)
        
        return max(nums[-1] + solveRobber(1, n-3), solveRobber(0, n-2))