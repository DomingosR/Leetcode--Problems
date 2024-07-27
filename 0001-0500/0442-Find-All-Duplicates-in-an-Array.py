class Solution(object):
    def findDuplicates(self, nums):
        duplicates = []

        for i in range(len(nums)):
            n = abs(nums[i])
            if nums[n-1] < 0:
                duplicates.append(n)
            nums[n-1] *= -1

        return duplicates
