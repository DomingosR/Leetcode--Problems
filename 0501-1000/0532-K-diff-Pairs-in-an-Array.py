class Solution(object):
    def findPairs(self, nums, k):
        numCounter = Counter(nums)
        numPairs = 0

        if k == 0:
            for num in numCounter:
                if numCounter[num] > 1:
                    numPairs += 1
        else:
            for num in numCounter:
                if num + k in numCounter:
                    numPairs += 1

        return numPairs
