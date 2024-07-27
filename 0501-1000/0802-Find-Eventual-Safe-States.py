class Solution(object):
    def eventualSafeNodes(self, graph):
        visitedNodes = [-1] * len(graph)
        returnVal = []
        
        def explore(i):
            visitedNodes[i] = 0
            for v in graph[i]:
                if visitedNodes[v] == 0 or (visitedNodes[v] == -1 and explore(v)): return True
            visitedNodes[i] = 1
            returnVal.append(i)
            return False
       
        for i in range(len(graph)):
            if visitedNodes[i] == -1: 
                explore(i)
        
        return sorted(returnVal)