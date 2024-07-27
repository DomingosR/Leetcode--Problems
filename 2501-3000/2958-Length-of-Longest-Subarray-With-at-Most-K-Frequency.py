class Solution(object):
    def maxSubarrayLength(self, nums, k):
        numCounter = Counter()
        j = -1
        longestGood = 0

        for i in range(len(nums)):
            num = nums[i]
            numCounter[num] += 1
            while numCounter[num] > k:
                j += 1
                numCounter[nums[j]] -= 1
            longestGood = max(longestGood, i - j)

        return longestGood
