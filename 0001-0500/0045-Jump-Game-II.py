class Solution(object):
    def jump(self, nums):
        if len(nums) == 1:
            return 0

        numJumps, prevMax, currMax = 0, 0, 0
        while currMax < len(nums)-1:
            currMax, prevMax = max([i + nums[i] for i in range(prevMax, currMax + 1)]), currMax
            numJumps += 1

        return numJumps
