class Solution(object):
    def destroyTargets(self, nums, space):
        valueCounter = Counter([num % space for num in nums])
        maxCount = max(valueCounter.values())
        return min([num for num in nums if valueCounter[num % space] == maxCount])