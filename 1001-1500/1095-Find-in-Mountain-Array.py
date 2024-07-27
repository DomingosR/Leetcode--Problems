class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        arrayVals = {}

        def getVal(index):
            if index not in arrayVals:
                arrayVals[index] = mountain_arr.get(index)
            return arrayVals[index]

        # Find peak of array
        leftIndex, rightIndex = 0, n-1
        while leftIndex < rightIndex:
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            if getVal(midIndex) < getVal(midIndex + 1):
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex
        peakIndex = leftIndex

        # Search value in left part of array
        leftIndex, rightIndex = 0, peakIndex
        while leftIndex <= rightIndex:
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            if getVal(midIndex) < target:
                leftIndex = midIndex + 1
            elif getVal(midIndex) > target:
                rightIndex = midIndex - 1
            else:
                return midIndex

        # Search value in right part of array
        leftIndex, rightIndex = peakIndex, n - 1
        while leftIndex <= rightIndex:
            midIndex = leftIndex + (rightIndex - leftIndex) // 2
            if getVal(midIndex) > target:
                leftIndex = midIndex + 1
            elif getVal(midIndex) < target:
                rightIndex = midIndex - 1
            else:
                return midIndex

        return -1
