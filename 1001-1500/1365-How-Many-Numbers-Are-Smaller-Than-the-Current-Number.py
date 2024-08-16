class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        numsCopy = deepcopy(nums)
        numsCopy.sort()
        return [bisect_left(numsCopy, num) for num in nums]