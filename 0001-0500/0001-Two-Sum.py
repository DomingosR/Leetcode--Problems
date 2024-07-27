class Solution(object):
    def twoSum(self, nums, target):
        valIndices = defaultdict(int)
        
        for i in range(len(nums)):
            if target - nums[i] in valIndices:
                return [valIndices[target - nums[i]], i]
            else:
                valIndices[nums[i]] = i