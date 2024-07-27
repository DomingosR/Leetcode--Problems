class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        p = 10**9 + 7
        
        def numOrders(nums):
            if len(nums) <= 2:
                return 1
            
            leftPart = [num for num in nums if num < nums[0]]
            rightPart = [num for num in nums if num > nums[0]]
            m = len(leftPart)
            n = len(rightPart)
            
            return comb(m+n, m) * numOrders(leftPart) * numOrders(rightPart)
            
        return (numOrders(nums) - 1) % p      