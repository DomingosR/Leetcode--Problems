class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        n = len(timeSeries)
        
        currentStart = timeSeries[0]
        currentEnd = timeSeries[0] + duration - 1
        numSeconds = 0
        
        for i in range(1, n):
            if timeSeries[i] <= currentEnd:
                currentEnd = timeSeries[i] + duration - 1
            else:
                numSeconds += currentEnd - currentStart + 1
                currentStart = timeSeries[i]
                currentEnd = timeSeries[i] + duration - 1
        
        numSeconds += currentEnd - currentStart + 1
        return numSeconds