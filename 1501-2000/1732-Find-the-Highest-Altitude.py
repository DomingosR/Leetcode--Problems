class Solution(object):
    def largestAltitude(self, gain):
        currentAltitude = 0
        maxAltitude = 0
        
        for i in range(len(gain)):
            currentAltitude += gain[i]
            maxAltitude = max(maxAltitude, currentAltitude)
            
        return maxAltitude