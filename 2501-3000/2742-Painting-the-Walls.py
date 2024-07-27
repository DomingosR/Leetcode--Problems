class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        largeNum = n * 10**6 + 1
        minCost = [0] + [largeNum] * n
        
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                minCost[j] = min(minCost[j], minCost[max(j - t - 1, 0)] + c)

        return minCost[n]