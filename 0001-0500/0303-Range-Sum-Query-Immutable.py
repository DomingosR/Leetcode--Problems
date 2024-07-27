class NumArray(object):
    def __init__(self, nums):
        self.partialSums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.partialSums[i+1] = self.partialSums[i] + nums[i]
             
    def sumRange(self, left, right):
        return self.partialSums[right + 1] - self.partialSums[left]