class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        nums1, nums2 = nums[:n//2], nums[(n+1)//2:][::-1]
        return max([sum(pair) for pair in zip(nums1, nums2)])