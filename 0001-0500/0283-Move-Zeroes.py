class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        zeroIndex = -1
        i = 0

        while i < n and zeroIndex < 0:
            if nums[i] == 0: zeroIndex = i
            i += 1
        
        if zeroIndex == -1:
            return nums
            
        while zeroIndex < n:
            nonZeroIndex = zeroIndex + 1
            while nonZeroIndex < n and nums[nonZeroIndex] == 0:
                nonZeroIndex += 1
            if nonZeroIndex < n:
                nums[zeroIndex] = nums[nonZeroIndex]
                nums[nonZeroIndex] = 0
            zeroIndex += 1
            while zeroIndex < n and nums[zeroIndex] != 0:
                zeroIndex += 1
        
        return nums