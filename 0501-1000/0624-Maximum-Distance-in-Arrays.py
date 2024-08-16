class Solution(object):
    def maxDistance(self, arrays):
        currentMin, currentMax, maxDiff = arrays[0][0], arrays[0][-1], 0
        
        for array in arrays[1:]:
            maxDiff = max(maxDiff, abs(array[0] - currentMax), abs(array[-1] - currentMin))
            currentMin, currentMax = min(array[0], currentMin), max(array[-1], currentMax)
            
        return maxDiff