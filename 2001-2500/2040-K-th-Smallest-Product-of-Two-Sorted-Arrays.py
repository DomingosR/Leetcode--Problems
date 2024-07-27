class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        def count(arr1, arr2, x):
            totalCount = 0
            j = len(arr2) - 1
            for i in range(len(arr1)):
                while j >= 0 and arr1[i] * arr2[j] > x:
                    j -= 1
                totalCount += j + 1
            return totalCount
        
        nums1Neg = [-n for n in nums1 if n < 0][::-1]
        nums1Zero = [n for n in nums1 if n == 0]
        nums1Pos = [n for n in nums1 if n > 0]
        nums2Neg = [-n for n in nums2 if n < 0][::-1]
        nums2Zero = [n for n in nums2 if n == 0]
        nums2Pos = [n for n in nums2 if n > 0]
        
        n1, n1Neg, n1Zero, n1Pos = len(nums1), len(nums1Neg), len(nums1Zero), len(nums1Pos)
        n2, n2Neg, n2Zero, n2Pos = len(nums2), len(nums2Neg), len(nums2Zero), len(nums2Pos)
        
        negCount = n1Neg * n2Pos + n1Pos * n2Neg
        zeroCount = n1Zero * n2 + n1 * n2Zero - n1Zero * n2Zero
        posCount = n1Neg * n2Neg + n1Pos * n2Pos
        
        if negCount < k <= negCount + zeroCount:
            return 0
        
        if k <= negCount:
            k = negCount + 1 - k
            list1A, list1B, list2A, list2B = nums1Neg, nums2Pos, nums2Neg, nums1Pos
            multiplier = -1
            
        if k > negCount + zeroCount:
            k -= (negCount + zeroCount)
            list1A, list1B, list2A, list2B = nums1Neg, nums2Neg, nums1Pos, nums2Pos
            multiplier = 1
            
        lowVal = 1
        highVal = max(list1A[-1] * list1B[-1] if list1A and list1B else 0, \
                      list2A[-1] * list2B[-1] if list2A and list2B else 0)
        while lowVal < highVal:
            midVal = lowVal + (highVal - lowVal) // 2
            if count(list1A, list1B, midVal) + count(list2A, list2B, midVal) < k:
                lowVal = midVal + 1
            else:
                highVal = midVal

        return multiplier * lowVal