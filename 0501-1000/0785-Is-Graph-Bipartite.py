class Solution(object):
    def isBipartite(self, graph): 
        nodeColor = {}
        
        def canColorNode(i):
            for j in graph[i]:
                if j in nodeColor:
                    if nodeColor[i] == nodeColor[j]:
                        return False
                else:
                    nodeColor[j] = 1 - nodeColor[i]
                    if not canColorNode(j):
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in nodeColor:
                nodeColor[i] = 0
                if not canColorNode(i):
                    return False
                
        return True