class Solution(object):
    def specialArray(self, nums):
        n = len(nums)
        if n == 1:
            return 1 if nums[0] >= 1 else -1

        nums.sort(reverse = True)
        lowIndex, highIndex = 0, n-1

        while lowIndex <= highIndex:
            midIndex = lowIndex + (highIndex - lowIndex) // 2
            if nums[midIndex] >= midIndex + 1 and (midIndex == n-1 or nums[midIndex + 1] < midIndex + 1):
                return midIndex + 1
            if nums[midIndex] < midIndex + 1:
                highIndex = midIndex - 1
            else:
                lowIndex = midIndex + 1

        return -1
