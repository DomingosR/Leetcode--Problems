class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        if not (nums1 and nums2):
            return 0

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        currentMaxLen = [0] * (n+1)
        for i in range(m):
            nextMaxLen = [0] * (n+1)
            for j in range(1, n+1):
                if nums1[i] == nums2[j-1]:
                    nextMaxLen[j] = currentMaxLen[j-1] + 1
                else:
                    nextMaxLen[j] = max(nextMaxLen[j-1], currentMaxLen[j])
            currentMaxLen = nextMaxLen

        return currentMaxLen[-1]
        