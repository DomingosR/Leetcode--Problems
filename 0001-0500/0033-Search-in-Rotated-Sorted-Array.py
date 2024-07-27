class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        leftIndex, rightIndex = 0, n-1

        while leftIndex <= rightIndex:
            midIndex = (rightIndex + leftIndex) // 2
            if nums[midIndex] == target:
                return midIndex

            if nums[midIndex] >= nums[leftIndex]:
                if nums[leftIndex] <= target < nums[midIndex]:
                    rightIndex = midIndex - 1
                else:
                    leftIndex = midIndex + 1

            else:
                if nums[midIndex] < target <= nums[rightIndex]:
                    leftIndex = midIndex + 1
                else:
                    rightIndex = midIndex - 1

        return -1
