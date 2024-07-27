class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        if target > nums[n-1]:
            return n
        if target == nums[n-1]:
            return n-1
        if target <= nums[0]:
            return 0

        leftIndex = 0
        rightIndex = n-1
        while nums[leftIndex] < target < nums[rightIndex] and rightIndex > leftIndex + 1:
            midIndex = (leftIndex + rightIndex) // 2
            if nums[midIndex] == target:
                return midIndex
            elif nums[midIndex] > target:
                rightIndex = midIndex
            else:
                leftIndex = midIndex

        return rightIndex