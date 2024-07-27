class Solution(object):
    def addedInteger(self, nums1, nums2):
        n = len(nums2)
        return (sum(nums2) - sum(nums1)) // n