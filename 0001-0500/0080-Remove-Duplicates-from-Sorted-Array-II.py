class Solution(object):
    def removeDuplicates(self, nums):
        currentVal, currentCount = nums[0] - 1, 0
        i, j = 0, 0
        
        for j in range(len(nums)):
            if nums[j] > currentVal:
                currentVal = nums[j]
                nums[i] = currentVal
                currentCount = 1
                i += 1
                
            elif currentCount == 1:
                nums[i] = currentVal
                currentCount = 2
                i += 1
        
        return i