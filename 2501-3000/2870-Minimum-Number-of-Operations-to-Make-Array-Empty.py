class Solution(object):
    def minOperations(self, nums):
        countVals = Counter(nums).values()

        def f(x):
            return (x + 2) // 3

        if 1 in countVals:
            return -1

        return sum(f(x) for x in countVals)
