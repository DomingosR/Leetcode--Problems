class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        # Function to compute maximum diameter of a subtree
        # (returns 0 if the given subset of vertices does not form a tree)
        def maxDistance(state):
            countEdges = 0
            countNodes = 0
            maxDist = 0
            
            for i in range(n):
                if (state >> i) & 1 == 0:        # Node i is not in graph
                    continue
                countNodes += 1
                for j in range(i + 1, n):
                    if (state >> j) & 1 == 0:    # Node j is not in graph 
                        continue 
                    if dist[i][j] == 1:
                        countEdges += 1
                    
                    maxDist = max(maxDist, dist[i][j])
                    
            if countEdges != countNodes - 1:     # This subgraph is not connected
                return 0
            
            return maxDist
        
        # Floyd Warshall algorithm to compute pairwise distances
        dist = [[n] * n for i in range(n)]
        for [node1, node2] in edges:
            dist[node1 - 1][node2 - 1] = 1
            dist[node2 - 1][node1 - 1] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Comnpute maximum distance for each possible subgraph
        numSubtrees = [0] * (n-1)
        for state in range(1, 2**n):
            maxDist = maxDistance(state)
            if maxDist > 0: 
                numSubtrees[maxDist - 1] += 1
        
        return numSubtrees