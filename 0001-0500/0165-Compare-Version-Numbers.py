class Solution(object):
    def compareVersion(self, version1, version2):
        nums1 = [int(num) for num in version1.split(".")]
        nums2 = [int(num) for num in version2.split(".")]
        n1, n2, i = len(nums1), len(nums2), 0
        
        for i in range(max(n1, n2)):
            val1 = nums1[i] if i < n1 else 0
            val2 = nums2[i] if i < n2 else 0
            if val1 < val2: return -1
            if val1 > val2: return 1
            
        return 0