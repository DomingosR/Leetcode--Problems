class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        finalStr = "0" * n
        
        for i in range(n):
            if nums[i][i] == "0":
                finalStr = finalStr[:i] + "1" + finalStr[i+1:]
                
        return finalStr