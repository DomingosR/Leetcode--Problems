class Solution(object):
    def minOperations(self, nums, x):
        n = len(nums)
        midSum = sum(nums) - x
        currentSum = 0
        maxLen = 0
        startIndex = 0
        sumFound = False

        for endIndex in range(n):
            currentSum += nums[endIndex]
            while startIndex <= endIndex and currentSum > midSum:
                currentSum -= nums[startIndex]
                startIndex += 1
            if currentSum == midSum:
                sumFound = True
                maxLen = max(maxLen, endIndex - startIndex + 1)
        
        return n - maxLen if sumFound else -1