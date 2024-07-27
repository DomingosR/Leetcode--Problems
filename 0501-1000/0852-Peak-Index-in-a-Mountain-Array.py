class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        leftIndex, rightIndex = 0, n-1
        
        while leftIndex < rightIndex:
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            
            if arr[midIndex] < arr[midIndex+1]:
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex
            
        return leftIndex