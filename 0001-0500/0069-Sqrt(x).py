class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
        
        lowVal = 1
        highVal = x // 2

        while lowVal < highVal:
            midVal = (lowVal + highVal) // 2
            if midVal * midVal <= x < (midVal + 1) * (midVal + 1):
                return midVal
            if midVal * midVal < x:
                lowVal = midVal + 1
            else:
                highVal = midVal - 1
        
        return lowVal
                