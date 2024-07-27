class Solution(object):
    def maximumStrongPairXor(self, nums):
        nums = sorted(list(set(nums)))
        maxXOR = 0
        
        for i in range(len(nums)):
            j = i
            while j < len(nums) and abs(nums[i] - nums[j]) <= nums[i]:
                maxXOR = max(maxXOR, nums[i] ^ nums[j])
                j += 1
        
        return maxXOR