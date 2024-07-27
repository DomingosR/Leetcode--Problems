class Solution(object):
    def minCost(self, n, cuts):
        cuts = [0] + sorted(cuts) + [n]
        numCuts = len(cuts)
        
        cutCost = [[0] * numCuts for _ in range(numCuts)]
        for i in range(2, numCuts):
            for j in range(numCuts - i):
                valList = [cutCost[j][m] + cutCost[m][j+i] for m in range(j+1, j+i)]
                cutCost[j][j+i] = min(valList) + cuts[i+j] - cuts[j]
        return cutCost[0][numCuts - 1]
        