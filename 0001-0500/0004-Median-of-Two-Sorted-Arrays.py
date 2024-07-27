class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        minVal = - 10**6 - 1
        maxVal = 10**6 + 1
        
        nums1 = [minVal] + nums1 + [maxVal]
        nums2 = [minVal] + nums2 + [maxVal]
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        if n1 < n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        
        def directionToMove(currentLeft1):
            currentLeft2 = n//2 - currentLeft1
            if nums1[currentLeft1 - 1] > nums2[currentLeft2]:
                return -1
            if nums2[currentLeft2 - 1] > nums1[currentLeft1]:
                return 1
            return 0

        minLeft1 = n//2 - n2 + 1
        maxLeft1 = n//2 - 1
        currentLeft1 = (minLeft1 + maxLeft1) // 2
        currentDir = directionToMove(currentLeft1)

        while currentDir != 0:
            if currentDir > 0:
                minLeft1 = currentLeft1 + 1
            else:
                maxLeft1 = currentLeft1 - 1

            currentLeft1 = (minLeft1 + maxLeft1) // 2
            currentDir = directionToMove(currentLeft1)
        
        currentLeft2 = n // 2 - currentLeft1
        leftVal = max(nums1[currentLeft1 - 1], nums2[currentLeft2 - 1])
        rightVal = min(nums1[currentLeft1], nums2[currentLeft2])

        return 1.0 * (leftVal + rightVal) / 2 if (n % 2 == 0) else rightVal