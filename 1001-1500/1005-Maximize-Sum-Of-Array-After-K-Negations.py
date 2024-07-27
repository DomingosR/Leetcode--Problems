class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        countNeg = bisect.bisect_left(nums, 0)

        if countNeg >= k:
            return -sum(nums[:k]) + sum(nums[k:])

        remaining = countNeg - k
        nums = [abs(num) for num in nums]
        return sum(nums) - (0 if remaining % 2 == 0 else 2 * min(nums))
