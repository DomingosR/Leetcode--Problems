class Solution(object):
    def majorityElement(self, nums):
        numCounter = Counter(nums)
        return [num for num in numCounter if numCounter[num] > len(nums) // 3]