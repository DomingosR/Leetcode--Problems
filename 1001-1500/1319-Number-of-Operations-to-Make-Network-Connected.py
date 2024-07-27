class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1: 
            return -1

        graph = [set() for i in range(n)]
        
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)
        nodeVisited = [0] * n

        def dfs(i):
            if nodeVisited[i]: 
                return 0
            nodeVisited[i] = 1
            for j in graph[i]: 
                dfs(j)
            auxVar = nodeVisited[i]
            return 1

        return sum([dfs(i) for i in range(n)]) - 1