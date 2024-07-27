class Solution(object):
    def validPartition(self, nums):
        n = len(nums)
        if n < 2:
            return False
        
        if n == 2:
            return nums[0] == nums[1]
        
        isValid = [0] * n
        if nums[-1] == nums[-2]:
            isValid[-2] = 1
            if nums[-1] == nums[-3]:
                isValid[-3] = 1
        else:
            if nums[-1] - nums[-2] == nums[-2] - nums[-3] == 1:
                isValid[-3] = 1
        
        if n >= 4:
            for i in range(n-4, -1, -1):
                if nums[i] == nums[i+1]:
                    if isValid[i+2]:
                        isValid[i] = 1
                    else:
                        if nums[i] == nums[i+2] and isValid[i+3]:
                            isValid[i] = 1
                elif nums[i+2] - nums[i+1] == nums[i+1] - nums[i] == 1 and isValid[i+3]:
                    isValid[i] = 1
        
        return isValid[0]