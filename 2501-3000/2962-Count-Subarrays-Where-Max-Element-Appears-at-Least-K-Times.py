class Solution(object):
    def countSubarrays(self, nums, k):
        maxVal = max(nums)
        numSubArrays = 0
        currentCount = 0
        j = 0
        for i in range(len(nums)):
            currentCount += (1 if nums[i] == maxVal else 0)
            while currentCount >= k:
                currentCount -= (1 if nums[j] == maxVal else 0)
                j += 1
            numSubArrays += j

        return numSubArrays
