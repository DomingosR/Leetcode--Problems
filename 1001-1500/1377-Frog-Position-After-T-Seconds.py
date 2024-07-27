class Solution(object):
    def frogPosition(self, n, edges, t, target):
        # Build graph
        neighbors = defaultdict(set)

        for v, w, in edges:
            neighbors[v].add(w)
            neighbors[w].add(v)

        # Compute shortest path to target vertex
        vertexQueue = deque([(1, 0)])
        numNeighbors = defaultdict(int)
        parent = defaultdict(int)

        while vertexQueue:
            currVertex, currDist = vertexQueue.pop()
            numNeighbors[currVertex] = len(neighbors[currVertex])
            if currVertex == target:
                break

            for v in neighbors[currVertex]:
                parent[v] = currVertex
                neighbors[v].remove(currVertex)
                vertexQueue.appendleft((v, currDist + 1))

        if t < currDist:
            return 0

        if t > currDist and numNeighbors[target] > 0:
            return 0

        currProb, currVertex = 1, target
        while currVertex != 1:
            currVertex = parent[currVertex]
            currProb *= (1.0 / numNeighbors[currVertex])

        return currProb
        
