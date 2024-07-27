class Solution(object):
    def checkSubarraySum(self, nums, k):
        sumList = {0: -1}
        if nums[0] % k != 0:
            sumList[nums[0] % k] = 0
        currentSum = nums[0] % k

        for i in range(1, len(nums)):
            currentSum = (currentSum + nums[i]) % k
            if currentSum not in sumList:
                sumList[currentSum] = i
            else:
                if i - sumList[currentSum] >= 2: return True

        return False
