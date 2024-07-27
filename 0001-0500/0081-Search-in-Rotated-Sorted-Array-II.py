class Solution(object):
    def search(self, nums, target):
        leftIndex, rightIndex = 0, len(nums) - 1

        while leftIndex <= rightIndex:
            midIndex = (rightIndex + leftIndex) // 2
            if nums[midIndex] == target:
                return True

            while leftIndex < midIndex and nums[leftIndex] == nums[midIndex]:
                leftIndex += 1

            if nums[leftIndex] <= nums[midIndex]:
                if nums[leftIndex] <= target < nums[midIndex]:
                    rightIndex = midIndex - 1
                else:
                    leftIndex = midIndex + 1
            else:
                if nums[midIndex] < target <= nums[rightIndex]:
                    leftIndex = midIndex + 1
                else:
                    rightIndex = midIndex - 1

        return False
