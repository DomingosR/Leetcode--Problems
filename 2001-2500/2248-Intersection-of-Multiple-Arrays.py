class Solution(object):
    def intersection(self, nums):
        numSets = [set(num) for num in nums]
        return sorted(list(set.intersection(*numSets)))