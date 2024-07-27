class Solution(object):
    def semiOrderedPermutation(self, nums):
        n = len(nums)
        index1, indexN = nums.index(1), nums.index(n)
        return n + index1 - indexN - 1 - (1 if indexN < index1 else 0)
