class MKAverage(object):

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.count = 0
        self.nums = []
        self.numQueue = deque()
        self.midSum = 0

    def addElement(self, num):
        if self.count == self.m:
            numToRemove = self.numQueue.pop()
            self.midSum -= min(max(numToRemove, self.nums[self.k]), self.nums[self.m - self.k - 1])
            pos = bisect_left(self.nums, numToRemove)
            self.nums.pop(pos)
            self.count -= 1
        
        if self.count >= 2 * self.k:
            self.midSum += min(max(num, self.nums[self.k - 1]), self.nums[self.count - self.k])
        
        pos = bisect_left(self.nums, num)
        self.nums[pos:pos] = [num]
        self.numQueue.appendleft(num)
        self.count += 1

    def calculateMKAverage(self):
        if self.count < self.m:
            return -1
        return self.midSum // (self.m - 2 * self.k)