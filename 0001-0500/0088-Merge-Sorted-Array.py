class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j, current = m-1, n-1, m+n-1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[current] = nums1[i]
                i -= 1
            else:
                nums1[current] = nums2[j]
                j -= 1
            current -= 1
        
        while j >= 0:
            nums1[current] = nums2[j]
            j -= 1
            current -= 1