class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        fullBottles = numBottles
        emptyBottles = 0
        bottlesDrunk = 0
        
        while fullBottles > 0:
            bottlesDrunk += fullBottles
            emptyBottles += fullBottles
            fullBottles = 0
            while emptyBottles >= numExchange:
                fullBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
        
        return bottlesDrunk
        