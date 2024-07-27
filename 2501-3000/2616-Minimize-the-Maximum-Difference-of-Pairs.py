class Solution(object):
    def minimizeMax(self, nums, p):
        nums.sort()
        n = len(nums)

        lowerBound, upperBound = 0, nums[-1] - nums[0]
        while lowerBound < upperBound:
            midVal = (lowerBound + upperBound) // 2
            numPairs = 0
            currentIndex = 1
            while currentIndex < n:
                if nums[currentIndex] - nums[currentIndex - 1] <= midVal:
                    numPairs += 1
                    currentIndex += 2
                else:
                    currentIndex += 1

            if numPairs >= p:
                upperBound = midVal
            else:
                lowerBound = midVal + 1

        return lowerBound
