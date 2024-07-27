class Solution(object):
    def garbageCollection(self, garbage, travel):
        totalLen = sum([len(indGarb) for indGarb in garbage])
        totalTravel = [0, 0, 0]
        cumTravel = 0
        
        for i in range(1, len(garbage)):
            cumTravel += travel[i-1]
            if "G" in garbage[i]: 
                totalTravel[0] = cumTravel
            if "P" in garbage[i]: 
                totalTravel[1] = cumTravel
            if "M" in garbage[i]: 
                totalTravel[2] = cumTravel
                
        return totalLen + sum(totalTravel)