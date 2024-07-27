class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        maxProd = [[0] * n for _ in range(m)]
        
        for j in range(n):
            for i in range(m):
                maxProd[i][j] = nums1[i] * nums2[j]
                if i > 0 and j > 0: 
                    maxProd[i][j] += max(maxProd[i-1][j-1], 0)
                if i > 0:
                    maxProd[i][j] = max(maxProd[i][j], maxProd[i-1][j])
                if j > 0:
                    maxProd[i][j] = max(maxProd[i][j], maxProd[i][j-1])

        return maxProd[-1][-1]