class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        lastElement = []
        currentCount = 0
        
        for i in range(n):
            currentPos = bisect.bisect_left(lastElement, nums[i])
            if currentPos == currentCount:
                lastElement.append(nums[i])
                currentCount += 1
            else:
                lastElement[currentPos] = nums[i]
                
        return currentCount