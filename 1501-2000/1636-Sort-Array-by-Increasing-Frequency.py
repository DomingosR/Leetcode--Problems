class Solution(object):
    def frequencySort(self, nums):
        numCounter = Counter(nums)
        nums.sort(key = lambda x: (numCounter[x], -x))
        return nums