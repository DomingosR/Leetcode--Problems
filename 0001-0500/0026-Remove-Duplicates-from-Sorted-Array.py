class Solution(object):
    def removeDuplicates(self, nums):
        currentVal = nums[0]
        nextPosition = 1

        for i in range(1, len(nums)):
            if nums[i] > currentVal:
                currentVal = nums[i]
                nums[nextPosition] = currentVal
                nextPosition += 1
            
        return nextPosition
                