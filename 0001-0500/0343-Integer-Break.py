class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1

        while n > 4:
            n -= 3
            product *= 3

        product *= n
        return product
