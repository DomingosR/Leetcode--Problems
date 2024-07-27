class Solution(object):
    def makeArrayIncreasing(self, nums1, nums2):
        m = len(nums1)
        if m == 1:
            return 0

        n = len(nums2)
        largeNo = 10**9 + 1
        maxSwaps = min(m, n)
        minVal = [[largeNo] * m for _ in range(maxSwaps + 1)]

        nums2.sort()
        minVal[0][0], minVal[1][0] = nums1[0], min(nums1[0], nums2[0])

        for j in range(1, m):
            for i in range(min(j+2, maxSwaps+1)):
                val1, val2 = largeNo, largeNo
                if minVal[i][j-1] < nums1[j]:
                    val1 = nums1[j]
                if i > 0:
                    auxInt = bisect_right(nums2, minVal[i-1][j-1])
                    if auxInt < n:
                        val2 = nums2[auxInt]
                minVal[i][j] = min(val1, val2)

        indices = [i for i in range(maxSwaps+1) if minVal[i][m-1] < largeNo]
        return indices[0] if indices else -1
