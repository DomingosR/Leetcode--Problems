class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        # Array with edges, first red, then blue
        allEdges = [[[], []] for i in range(n)]
        numEdges = len(red_edges) + len(blue_edges)

        for i, j in red_edges:
            allEdges[i][0].append(j)
        for i, j in blue_edges:
            allEdges[i][1].append(j)
        
        # Array with minimum distance arriving from red edge versus blue edge
        minDistance = [[0, 0]] + [[numEdges+1, numEdges+1] for i in range(n-1)]

        vertexQueue = deque()
        vertexQueue.appendleft([0, 0])  # Process red edges out of vertex 0
        vertexQueue.appendleft([0, 1])  # Process blue edges out of vertex 0

        while vertexQueue:
            i, c = vertexQueue.pop()
            for j in allEdges[i][c]:
                if minDistance[j][1-c] == numEdges + 1:
                    minDistance[j][1-c] = minDistance[i][c] + 1
                    vertexQueue.appendleft([j, 1-c])

        return [dist if dist < numEdges + 1 else -1 for dist in map(min, minDistance)]fs