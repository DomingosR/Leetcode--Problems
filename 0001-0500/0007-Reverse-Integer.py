class Solution(object):
    def reverse(self, x):
        minVal = -2**31
        maxVal = -minVal - 1

        sign = -1 if x < 0 else 1
        absVal = sign * x
        reversed = int(str(absVal)[ : : -1])
        auxVal = sign * reversed
        return  auxVal * (minVal <= auxVal <= maxVal)
