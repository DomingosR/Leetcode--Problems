class Solution(object):
    def findMaxLength(self, nums):
        currentSum = 0
        sumLocation = defaultdict(int)
        sumLocation[0] = -1
        maxLen = 0

        for i, num in enumerate(nums):
            currentSum += (1 if num == 1 else -1)
            if currentSum in sumLocation:
                maxLen = max(maxLen, i - sumLocation[currentSum])
            else:
                sumLocation[currentSum] = i

        return maxLen
