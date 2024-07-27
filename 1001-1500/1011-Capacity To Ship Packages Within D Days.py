class Solution(object):
    def shipWithinDays(self, weights, days):
        lowerVal = max(weights)
        higherVal = sum(weights)

        while lowerVal < higherVal:
            midVal = (lowerVal + higherVal) // 2
            containers = 1
            currentWeight = 0
            for w in weights:
                currentWeight += w
                if currentWeight > midVal:
                    containers += 1
                    currentWeight = w
            
            if containers > days:
                lowerVal = midVal + 1
            else:
                higherVal = midVal
        
        return lowerVal