class RecentCounter(object):
    def __init__(self):
        self.numCalls = 0
        self.callTimes = []
        heapify(self.callTimes)

    def ping(self, t):
        while self.callTimes and t - self.callTimes[0] > 3000:
            heappop(self.callTimes)
            self.numCalls -= 1
        heappush(self.callTimes, t)
        self.numCalls += 1
        return self.numCalls
