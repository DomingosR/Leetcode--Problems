class Solution(object):
    def combinationSum3(self, k, n):
        def combs(n, k, maxVal):
            if maxVal <= 0 or n <= 0:
                return []
            if k == 1:
                return [[n]] if n <= maxVal else []
            return [[currVal] + prevComb
                    for currVal in range(1, maxVal+1)
                    for prevComb in combs(n-currVal, k-1, currVal - 1)]
        
        return combs(n, k, 9)