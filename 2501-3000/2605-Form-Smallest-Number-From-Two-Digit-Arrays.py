class Solution(object):
    def minNumber(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        intersection = set1 & set2
        
        if intersection:
            return min(intersection)
        
        min1, min2 = min(set1), min(set2)
        return 10 * min(min1, min2) + max(min1, min2)