class Solution(object):
    def maxSlidingWindow(self, nums, k):
        highestIndices = deque()
        slidingMax = []

        for i, n in enumerate(nums):
            while highestIndices and nums[highestIndices[-1]] < n:
                highestIndices.pop()
            highestIndices.append(i)
            if highestIndices[0] == i - k:
                highestIndices.popleft()
            if i >= k - 1:
                slidingMax.append(nums[highestIndices[0]])

        return slidingMax