class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        tiles.sort(key = lambda x: x[0])
        intervals = []
        
        for left, right in tiles:
            if intervals and left == intervals[-1]:
                intervals.pop()
                intervals.append(right + 1)
            else:
                intervals += [left, right + 1]
                
        cumLength = [0] * len(intervals)
        
        for i in range(1, len(intervals)):
            if i % 2:
                cumLength[i] = cumLength[i-1] + (intervals[i] - intervals[i-1])
            else:
                cumLength[i] = cumLength[i-1]
        
        n = len(intervals) // 2
        totalLength = 0
        
        for i in range(n):
            startLength = cumLength[2 * i]
            
            endPoint = intervals[2 * i] + carpetLen
            index = bisect_right(intervals, endPoint)
                                 
            if index == 2 * n:
                endLength = cumLength[-1]
            elif index % 2:
                endLength = endPoint - intervals[index - 1] + cumLength[index - 1]
            else:
                endLength = cumLength[index - 1]
            
            totalLength = max(totalLength, endLength - startLength)
                                 
        return totalLength