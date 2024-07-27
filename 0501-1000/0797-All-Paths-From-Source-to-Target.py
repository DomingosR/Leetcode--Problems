class Solution(object):
    def allPathsSourceTarget(self, graph):
        returnVal = []
        n = len(graph)
        pathsToExplore = deque()
        for i in graph[0]:
            pathsToExplore.appendleft([0, i])
        
        while pathsToExplore:
            nextPath = pathsToExplore.pop()
            lastNode = nextPath[-1]
            if lastNode == n-1:
                returnVal.append(nextPath)
            else:
                for i in graph[lastNode]:
                    pathsToExplore.append(nextPath + [i])
        
        return returnVal