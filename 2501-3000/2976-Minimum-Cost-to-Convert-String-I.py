class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        transitionCost = [[float('inf')] * 26 for _ in range(26)]
        baseline = ord('a')
        
        for i in range(26):
            transitionCost[i][i] = 0
        
        for i in range(len(original)):
            originalIndex = ord(original[i]) - baseline
            changedIndex = ord(changed[i]) - baseline
            transitionCost[originalIndex][changedIndex] = \
                min(cost[i], transitionCost[originalIndex][changedIndex])
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    transitionCost[i][j] = min(transitionCost[i][j], \
                            transitionCost[i][k] + transitionCost[k][j])
        
        totalCost = 0
        
        for i in range(len(source)):
            originalIndex = ord(source[i]) - baseline
            changedIndex = ord(target[i]) - baseline
            if transitionCost[originalIndex][changedIndex] == float('inf'):
                return -1
            totalCost += transitionCost[originalIndex][changedIndex]
            
        return totalCost