class Solution(object):
    def minCost(self, colors, neededTime):
        totalTime = 0
        largeVal = 10**5 + 1
        
        currentCount = 0
        currentSum = 0
        currentMax = 0
        
        for i in range(len(colors)):
            currentCount += 1
            currentSum += neededTime[i]
            currentMax = max(currentMax, neededTime[i])
            
            if i == len(colors)-1 or colors[i] != colors[i+1]:
                if currentCount > 1:
                    totalTime += currentSum - currentMax
                currentSum = 0
                currentCount = 0
                currentMax = 0
                    
        return totalTime