class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        numCount = len(nums)
        leftSum = nums[0]
        leftCount = 1
        rightSum = sum(nums[1:])
        rightCount = numCount - 1
        
        def currentAvg(sum, count):
            if count == 0:
                return 0
            return sum // count

        def absDiff(leftSum, leftCount, rightSum, rightCount):
            return abs(currentAvg(leftSum, leftCount) - currentAvg(rightSum, rightCount))
        
        minDiff = absDiff(leftSum, leftCount, rightSum, rightCount)
        currentIndex = 0
        
        for i in range(1, numCount):
            leftSum += nums[i]
            rightSum -= nums[i]
            leftCount += 1
            rightCount -= 1
            currentDiff = absDiff(leftSum, leftCount, rightSum, rightCount)
            if currentDiff < minDiff:
                minDiff = currentDiff
                currentIndex = i
                
        return currentIndex 