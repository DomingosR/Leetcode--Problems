class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        maxValQueue = deque()
        maxSum = -10**4-1

        for i in range(len(nums)):
            while maxValQueue and maxValQueue[0][1] < i-k:
                maxValQueue.popleft()
            currSum = nums[i]
            if maxValQueue and maxValQueue[0][0] > 0:
                currSum += maxValQueue[0][0]
            while maxValQueue and maxValQueue[-1][0] <= currSum:
                maxValQueue.pop()
            maxValQueue.append((currSum, i))
            maxSum = max(currSum, maxSum)

        return maxSum
