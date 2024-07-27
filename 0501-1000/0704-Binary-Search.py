class Solution(object):
    def search(self, nums, target):
        leftIndex = 0
        rightIndex = len(nums) - 1

        while 1:
            if leftIndex > rightIndex or target < nums[leftIndex] or target > nums[rightIndex]:
                return -1

            midIndex = (leftIndex + rightIndex) // 2
            if nums[midIndex] == target:
                return midIndex
            if nums[midIndex] < target:
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex - 1
