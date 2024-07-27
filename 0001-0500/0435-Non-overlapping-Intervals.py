class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        currEnd = -5 * 10**4 - 1

        removedCount = 0
        intervals.sort(key = lambda x: x[1])

        for start, end in intervals:
            if start >= currEnd:
                currEnd = end
            else:
                removedCount += 1

        return removedCount
        
