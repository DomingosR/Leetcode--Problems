class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        maxLow = candidates
        minHigh = max(n - candidates, candidates)
        totalCost = 0
        possibleChoices = []
        heapify(possibleChoices)
        
        for i in range(maxLow):
            heappush(possibleChoices, (costs[i], i))
            
        for i in range(minHigh, n): 
            heappush(possibleChoices, (costs[i], i))
            
        for i in range(k):
            cost, i = heappop(possibleChoices)
            totalCost += cost
            if maxLow < minHigh:
                if i < maxLow:
                    heappush(possibleChoices, (costs[maxLow], maxLow))
                    maxLow += 1
                else:
                    minHigh -= 1
                    heappush(possibleChoices, (costs[minHigh], minHigh))
        
        return totalCost