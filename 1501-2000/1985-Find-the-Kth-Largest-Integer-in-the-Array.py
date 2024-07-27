class Solution(object):
    def kthLargestNumber(self, nums, k):
        nums = sorted([int(num) for num in nums], reverse = True)
        return str(nums[k-1])