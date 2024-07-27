class UndergroundSystem(object):

    def __init__(self):
        self.entryTime = defaultdict(list)
        self.totalTripTime = defaultdict(int)
        self.numTrips = defaultdict(int)

    def checkIn(self, id, stationName, t):
        self.entryTime[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        entryStation, entryTime = self.entryTime[id]
        self.totalTripTime[(entryStation, stationName)] += (t - entryTime)
        self.numTrips [(entryStation, stationName)] += 1
        self.entryTime[id] = []

    def getAverageTime(self, startStation, endStation):
        totalTime = self.totalTripTime[(startStation, endStation)]
        tripCount = self.numTrips[(startStation, endStation)]
        return 1.0 * totalTime / tripCount