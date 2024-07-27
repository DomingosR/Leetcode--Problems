class RandomizedSet(object):
    def __init__(self):
        self.numVals = []
        self.numPosition = {}

    def insert(self, val):
        if val not in self.numVals:
            self.numVals.append(val)
            self.numPosition[val] = len(self.numVals) - 1
            return True
        return False

    def remove(self, val):
        if val in self.numPosition:
            lastNum = self.numVals.pop()
            if lastNum != val:
                nPos = self.numPosition[val]
                self.numVals[nPos] = lastNum
                self.numPosition[lastNum] = nPos
            self.numPosition.pop(val)
            return True
        return False

    def getRandom(self):
        return self.numVals[random.randint(0, len(self.numVals)-1)]
