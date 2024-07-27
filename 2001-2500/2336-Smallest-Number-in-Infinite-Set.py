class SmallestInfiniteSet(object):

    def __init__(self):
        self.minNum = 1
        self.addedBack = []
        heapq.heapify(self.addedBack)

    def popSmallest(self):
        if self.addedBack:
            return heapq.heappop(self.addedBack)
        else:
            self.minNum += 1
            return self.minNum - 1

    def addBack(self, num):
        if num < self.minNum:
            if num not in self.addedBack:
                heapq.heappush(self.addedBack, num)