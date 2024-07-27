class Solution(object):
    def minimumOperations(self, nums):
        posNumCounter = Counter([nums[i] for i in range(len(nums)) if nums[i] > 0])
        return len(posNumCounter)
        
