class Solution(object):
    def minOperations(self, nums, k):
        return len([num for num in nums if num < k])