class Solution(object):
    def maximalNetworkRank(self, n, roads):
        maxRank = 0
        adjNodes = defaultdict(set)
        for i, j in roads:
            adjNodes[i].add(j)
            adjNodes[j].add(i)
            
        for i in range(n-1):
            for j in range(i+1, n):
                currentRank = len(adjNodes[i]) + len(adjNodes[j]) - (j in adjNodes[i])
                maxRank = max(maxRank, currentRank)
        
        return maxRank