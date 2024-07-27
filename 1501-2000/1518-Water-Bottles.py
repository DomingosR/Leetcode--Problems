class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        fullBottles = numBottles
        emptyBottles = 0
        bottlesDrunk = 0
        
        while fullBottles > 0 or emptyBottles >= numExchange:
            bottlesDrunk += fullBottles
            emptyBottles += fullBottles
            fullBottles, emptyBottles = emptyBottles // numExchange, emptyBottles % numExchange
        
        return bottlesDrunk