class Solution(object):
    def findContentChildren(self, greed, size):
        greed.sort()
        size.sort()
        
        greedPtr, sizePtr = len(greed) - 1, len(size) - 1
        numAssigned = 0
        
        while greedPtr >= 0 and sizePtr >= 0:
            if size[sizePtr] >= greed[greedPtr]:
                numAssigned += 1
                sizePtr -= 1    
            greedPtr -= 1
            
        return numAssigned