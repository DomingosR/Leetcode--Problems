class Solution(object):
    def myPow(self, x, n):
        if x == 0:
            return 0

        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1.0/x

        result = 1
        if n % 2 == 1:
            result = x
            n -= 1

        return result * self.myPow(x * x, n // 2)
