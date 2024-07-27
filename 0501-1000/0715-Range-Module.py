class RangeModule(object):

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        l = bisect_left(self.intervals, left)
        r = bisect_right(self.intervals, right)
        
        toInsert = []
        if l % 2 == 0: toInsert.append(left)
        if r % 2 == 0: toInsert.append(right)

        self.intervals[l:r] = toInsert
        
    def queryRange(self, left, right):
        l = bisect_right(self.intervals, left)
        r = bisect_left(self.intervals, right)
        if l != r:
            return False
        return l % 2 == r % 2 == 1
        

    def removeRange(self, left, right):
        l = bisect_left(self.intervals, left)
        r = bisect_right(self.intervals, right)
        
        toInsert = []
        if l % 2 == 1: toInsert.append(left)
        if r % 2 == 1: toInsert.append(right)

        self.intervals[l:r] = toInsert    