class Solution(object):
    def commonFactors(self, a, b):
        def gcd(a, b):
            while a % b != 0:
                a, b = b, a % b
            return b

        return sum([1 for n in range(1, gcd(a,b) + 1) if ((a % n == 0) and (b % n == 0))])
