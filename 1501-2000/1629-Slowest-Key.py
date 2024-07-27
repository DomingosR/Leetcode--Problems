class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        releaseTimes = [0] + releaseTimes
        currentMaxKey, currentMaxLength = "", 0
        
        for i in range(len(keysPressed)):
            currentKey = keysPressed[i]
            currentLength = releaseTimes[i+1] - releaseTimes[i]
            
            if currentLength > currentMaxLength or (currentLength == currentMaxLength and currentKey > currentMaxKey):
                currentMaxKey = currentKey
                currentMaxLength = currentLength
                
        return currentMaxKey