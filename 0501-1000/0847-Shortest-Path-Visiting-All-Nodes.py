class Solution(object):
    def shortestPathLength(self, graph):
        numNodes = len(graph)
        nodeMask = [(1 << i) for i in range(numNodes)]
        allNodes = (1 << numNodes) - 1
        
        nodeQueue = deque([(i, nodeMask[i]) for i in range(numNodes)])
        visitedStates = [{nodeMask[i]} for i in range(numNodes)]
        numSteps = 0
        
        while nodeQueue:
            queueCount = len(nodeQueue)
            while queueCount:
                currentNode, visitedNodes = nodeQueue.pop()
                if visitedNodes == allNodes:
                    return numSteps
                
                for nextNode in graph[currentNode]:
                    nextVisited = visitedNodes | nodeMask[nextNode]
                    if nextVisited == allNodes:
                        return numSteps + 1
                    if nextVisited not in visitedStates[nextNode]:
                        visitedStates[nextNode].add(nextVisited)
                        nodeQueue.appendleft((nextNode, nextVisited))
                
                queueCount -= 1
            
            numSteps += 1
            
        return inf