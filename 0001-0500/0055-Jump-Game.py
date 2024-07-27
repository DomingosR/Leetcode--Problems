class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        if n == 1:
            return True

        currentIndex = 0
        maxIndex = nums[0]

        while maxIndex > currentIndex:
            if maxIndex >= n-1:
                return True
            reachable = [i + nums[i] for i in range(currentIndex, maxIndex+1)]
            currentIndex = maxIndex
            maxIndex = max(reachable)

        return False
