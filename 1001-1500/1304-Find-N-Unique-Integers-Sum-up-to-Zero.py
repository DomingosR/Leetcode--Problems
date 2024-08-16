class Solution(object):
    def sumZero(self, n):
        totalSum = (n - 1) * n // 2
        return list(range(1, n)) + [- totalSum]