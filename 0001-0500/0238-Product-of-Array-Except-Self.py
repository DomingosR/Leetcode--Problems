class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        finalProduct = [1] * n
        
        for i in range(n-1):
            finalProduct[i + 1] = finalProduct[i] * nums[i]
            
        rightProduct = 1
        for i in range(n-1, -1 , -1):
            finalProduct[i] *= rightProduct
            rightProduct *= nums[i]
            
        return finalProduct