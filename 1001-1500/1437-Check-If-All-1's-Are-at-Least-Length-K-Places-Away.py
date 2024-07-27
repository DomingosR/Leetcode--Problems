class Solution(object):
    def kLengthApart(self, nums, k):
        onesPositions = [i for i in range(len(nums)) if nums[i] == 1]

        if len(onesPositions) <= 1:
            return True
        
        posDiff = [(onesPositions[i+1] - onesPositions[i]) for i in range(len(onesPositions) - 1)]
        return min(posDiff) > k