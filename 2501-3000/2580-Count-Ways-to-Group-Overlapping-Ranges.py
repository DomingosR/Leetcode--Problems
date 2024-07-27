class Solution(object):
    def countWays(self, ranges):
        p = 10 ** 9 + 7
        unitedIntervals = []
        
        for start, end in ranges:
            left = bisect_left(unitedIntervals, start)
            right = bisect_right(unitedIntervals, end)
            toInsert = []
            if left % 2 == 0:
                toInsert.append(start)
            if right % 2 == 0:
                toInsert.append(end)
            unitedIntervals[left:right] = toInsert
            
        n = len(unitedIntervals) // 2
        
        return (2 ** n) % p