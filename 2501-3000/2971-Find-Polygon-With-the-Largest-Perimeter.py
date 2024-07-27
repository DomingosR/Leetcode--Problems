class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        n, total = len(nums), sum(nums)

        for side in nums[n-1:1:-1]:
            if side < total - side:
                return total
            total -= side

        return -1
