class Solution(object):
    def minReorder(self, n, connections):
        connectedEdges = defaultdict(list)
        
        # First element of pair is the connected vertex
        # Second element is whether the current vertex is
        #    the source of the edge
        for v1, v2 in connections:
            connectedEdges[v1].append((v2, 1))
            connectedEdges[v2].append((v1, 0))
        
        visitedVertices = [1] + [0] * (n - 1)
        numReversed = 0
        vertexQueue = deque()
        vertexQueue.appendleft(0)

        while vertexQueue:
            currentVertex = vertexQueue.pop()
            for nextVertex, source in connectedEdges[currentVertex]:
                if visitedVertices[nextVertex] == 0:
                    visitedVertices[nextVertex] = 1
                    vertexQueue.appendleft(nextVertex)
                    if source == 1:
                        numReversed += 1
        
        return numReversed