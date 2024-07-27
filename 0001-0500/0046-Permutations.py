class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        returnVal = []
        for i, n in enumerate(nums):
            for prevPerm in self.permute(nums[:i] + nums[i+1:]):
                returnVal.append([n] + prevPerm)

        return returnVal  
