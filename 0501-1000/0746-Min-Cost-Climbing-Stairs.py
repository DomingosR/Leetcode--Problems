class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost1, cost2 = cost[n-1], 0

        for i in range(n-2, -1, -1):
            cost1, cost2 = cost[i] + min(cost1, cost2), cost1

        return min(cost1, cost2)
