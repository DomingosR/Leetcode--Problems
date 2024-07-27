class Solution(object):
    def carFleet(self, target, position, speed):
        travelInfo = list(map(list, zip(position, speed)))
        travelInfo.sort(key = lambda x: -x[0])
        
        numFleets = 0
        currentArrival = -1
        
        for carPos, carSpeed in travelInfo:
            if carPos + currentArrival * carSpeed < target:
                numFleets += 1
                currentArrival = 1.0 * (target - carPos) / carSpeed
                
        return numFleets