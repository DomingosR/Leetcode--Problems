class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        intersection = set(nums1) & set(nums2)
        count1 = len([1 for num in nums1 if num in intersection])
        count2 = len([1 for num in nums2 if num in intersection])
        return [count1, count2]