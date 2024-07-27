import heapq

def minNumRefuelStops(target, initialFuel, stationStops):
    fuelHeap = []
    numStops, i = 0, 0
    currentFuel = initialFuel

    while currentFuel < target:
        while i < len(stationStops) and stationStops[i][0] <= currentFuel:
            heapq.heappush(fuelHeap, -stationStops[i][1])
            i += 1
        if not fuelHeap: 
            return -1
        currentFuel += -heapq.heappop(fuelHeap)
        numStops += 1

    return numStops

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        return minNumRefuelStops(target, startFuel, stations)