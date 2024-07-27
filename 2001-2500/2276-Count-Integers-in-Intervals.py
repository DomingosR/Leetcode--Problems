class CountIntervals(object):
    def __init__(self):
        self.leftEnd = []
        self.rightEnd = []
        self.intCount = 0

    def add(self, left, right):
        right += 1
        n = len(self.leftEnd)
        leftInsert = bisect.bisect_left(self.leftEnd, left)
        rightInsert = bisect.bisect_right(self.rightEnd, right)
        
        startIndex = max(0, leftInsert - 1)
        endIndex = min(rightInsert + 1, n - 1)
        startOverlap = n
        endOverlap = -1

        for i in range(startIndex, endIndex + 1):
            if self.leftEnd[i] <= right and left <= self.rightEnd[i]:
                left = min(left, self.leftEnd[i])
                right = max(right, self.rightEnd[i])
                startOverlap = min(startOverlap, i)
                endOverlap = max(endOverlap, i)
                self.intCount -= (self.rightEnd[i] - self.leftEnd[i])
        
        self.intCount += (right - left)
        if startOverlap < n:
            self.leftEnd = self.leftEnd[:startOverlap] + [left] + self.leftEnd[endOverlap + 1:]
            self.rightEnd = self.rightEnd[:startOverlap] + [right] + self.rightEnd[endOverlap + 1:]
        else:
            self.leftEnd.insert(leftInsert, left)
            self.rightEnd.insert(rightInsert, right)

    def count(self):
        return self.intCount