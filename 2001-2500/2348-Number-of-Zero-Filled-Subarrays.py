class Solution(object):
    def zeroFilledSubarray(self, nums):
        n = len(nums)
        numArrays = 0
        currentLen = 0

        for i in range(n):
            if nums[i] == 0:
                currentLen += 1
            else:
                numArrays += currentLen * (currentLen + 1) // 2
                currentLen = 0
        
        numArrays += currentLen * (currentLen + 1) // 2
        return numArrays