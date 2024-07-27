class Solution(object):
    def insert(self, intervals, newInterval):
        n = len(intervals)
        if n == 0:
            return [newInterval]

        leftEnd, rightEnd = list(map(list, zip(*intervals)))
        newLeft, newRight = newInterval

        leftIns = bisect_right(leftEnd, newLeft)
        rightIns = bisect_left(rightEnd, newRight)

        if leftIns > 0 and newLeft <= rightEnd[leftIns-1]:
            newLeft = leftEnd[leftIns - 1]
            leftIns -= 1

        if rightIns < n and newRight >= leftEnd[rightIns]:
            newRight = rightEnd[rightIns]
            rightIns += 1

        return intervals[:leftIns] + [[newLeft, newRight]] + intervals[rightIns:]
