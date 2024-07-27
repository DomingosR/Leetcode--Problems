def countSmallerAfterSelf(inputArray):
        if len(inputArray) < 1:
            return []

        auxArray = []
        countArray = []

        for currentNum in inputArray[ : : -1]:
            index = bisect.bisect_left(auxArray, currentNum)
            countArray.append(index)
            auxArray.insert(index, currentNum)

        return countArray[ : : -1]

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        return countSmallerAfterSelf(nums)