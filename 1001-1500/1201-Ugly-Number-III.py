class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        def gcd(n1, n2):
            while n2 > 0:
                n1, n2 = n2, n1 % n2
            return n1

        def uglyCount(num):
            numA, numB, numC = num // a, num // b, num // c
            auxAB, auxAC, auxBC = a * b // gcd(a, b), a * c // gcd(a, c), b * c // gcd(b, c)
            numAB, numAC, numBC = num // auxAB, num // auxAC, num // auxBC
            auxABC = auxAB * c // gcd(auxAB, c)
            numABC = num // auxABC

            return numA + numB + numC - numAB - numAC - numBC + numABC
        
        minVal = 1
        maxVal = n * max(a, b, c)

        while minVal < maxVal:
            midVal = (minVal + maxVal) // 2
            if uglyCount(midVal) < n:
                minVal = midVal + 1
            else:
                maxVal = midVal

        return minVal