class Solution(object):
    def minOperations(self, nums1, nums2):
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        
        if sum1 > sum2:
            nums1, nums2, sum1, sum2 = nums2, nums1, sum2, sum1
        
        overallDiff, possibleChanges, totalPossible = sum2 - sum1, [0] * 6, 0
        
        for num in nums1:
            currentDiff = 6 - num
            totalPossible += currentDiff
            possibleChanges[currentDiff] += 1
        
        for num in nums2:
            currentDiff = num - 1
            totalPossible += currentDiff
            possibleChanges[currentDiff] += 1
            
        if totalPossible < overallDiff:
            return -1
        
        numOps, i = 0, 5
        
        while True:
            if overallDiff > possibleChanges[i] * i:
                overallDiff -= possibleChanges[i] * i
                numOps += possibleChanges[i]
                i -= 1
            else:
                return numOps + (overallDiff + i - 1) // i