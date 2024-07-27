class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()

        if all([nums[3*i+2] - nums[3*i] <= k for i in range(len(nums) // 3)]):
            return [nums[3*i:3*i+3] for i in range(len(nums)//3)]
        return []
