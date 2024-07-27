class Solution(object):
    def maxValue(self, n, index, maxSum):
        # Throughout this solution we work with non-negative values, so
        # we subtract n from maxSum to start in order to adjust for this.
        
        # Returns minimum sum consistent with val being the peak at index
        def minSumVal(val):
            if val > index:
                sumLeft = (2 * val - index) * (index + 1) // 2
            else:
                sumLeft = val * (val + 1) //2
                
            if n - index < val:
                sumRight = (2 * val - n + index) * (n - index - 1) // 2
            else:
                sumRight = (val - 1) * val // 2
            
            return sumLeft + sumRight

        maxSum -= n
        lowVal, highVal = 0, maxSum
        
        while lowVal < highVal:
            midVal = (lowVal + highVal + 1) // 2
            if minSumVal(midVal) <= maxSum:
                lowVal = midVal
            else:
                highVal = midVal - 1
                
        return lowVal + 1