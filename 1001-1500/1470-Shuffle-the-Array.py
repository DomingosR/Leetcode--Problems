class Solution(object):
    def shuffle(self, nums, n):
        returnVal = []
        for i in range(n):
            returnVal.append(nums[i])
            returnVal.append(nums[n+i])
        
        return returnVal