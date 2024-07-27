class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        
        # Find longest non-decreasing subarray on left
        leftPtr = 0
        while leftPtr < n-1 and arr[leftPtr] <= arr[leftPtr + 1]:
            leftPtr += 1

        if leftPtr == n-1:
            return 0
        minVal = n - leftPtr - 1
        
        # Find longest non-decreasing subarray on right
        rightPtr = n-1
        while rightPtr > 0 and arr[rightPtr] >= arr[rightPtr - 1]:
            rightPtr -= 1
        minVal = min(minVal, rightPtr)
        
        # Analyze subarrays to remove in the middle of the original array
        if arr[0] <= arr[-1]:
            while arr[rightPtr] < arr[0]:
                rightPtr += 1
                
            leftPtr = 0

            while rightPtr < n:
                while arr[leftPtr + 1] <= arr[rightPtr] and arr[leftPtr] <= arr[leftPtr + 1]:
                    leftPtr += 1
                minVal = min(minVal, rightPtr - leftPtr - 1)
                rightPtr += 1

        return minVal