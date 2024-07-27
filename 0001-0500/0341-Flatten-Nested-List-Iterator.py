class NestedIterator(object):
    numArray = []
    currentIndex = -1

    def __init__(self, nestedList):
        def extractValues(nestedList):
            for indEntry in nestedList:
                if indEntry.isInteger():
                    self.numArray.append(indEntry.getInteger())
                else:
                    extractValues(indEntry.getList())

        self.numArray = []
        extractValues(nestedList)
        self.currentIndex = 0

    def next(self):
        self.currentIndex += 1
        return self.numArray[self.currentIndex - 1]

    def hasNext(self):
        return self.currentIndex < len(self.numArray)
