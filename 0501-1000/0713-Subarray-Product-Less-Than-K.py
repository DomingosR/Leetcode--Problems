class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0:
            return 0
        
        n = len(nums)
        subArrayCount = 0
        j = 0
        currentProduct = 1
        
        for i in range(n):
            currentProduct *= nums[i]
            while j <= i and currentProduct >= k:
                currentProduct //= nums[j]
                j += 1
            subArrayCount += (i - j + 1)
            
        return subArrayCount