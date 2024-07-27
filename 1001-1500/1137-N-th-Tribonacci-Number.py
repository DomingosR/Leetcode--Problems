class Solution(object):
    def tribonacci(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        previous, last, current = 0, 1, 1

        for i in range(n-2):
            previous, last, current = last, current, previous + last + current

        return current
