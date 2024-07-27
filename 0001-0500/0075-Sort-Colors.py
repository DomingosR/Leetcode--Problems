class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        i, j = 0, 0
        
        while j < n:
            if nums[j] == 0:
                swap(i, j)
                i += 1
            j += 1
            
        j = i
        
        while j < n:
            if nums[j] == 1:
                swap(i, j)
                i += 1
            j += 1
            
        return nums