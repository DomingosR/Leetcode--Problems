class Solution(object):
    def merge(self, intervals):
        intervalInfo = intervals[0]
        
        for left, right in intervals[1:]:
            l = bisect_left(intervalInfo, left)
            r = bisect_right(intervalInfo, right)

            toInsert = []
            if l % 2 == 0: toInsert.append(left)
            if r % 2 == 0: toInsert.append(right)

            intervalInfo[l:r] = toInsert
        
        return [intervalInfo[2*i:2*i+2] for i in range(len(intervalInfo) // 2)]