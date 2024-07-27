def criticalConnections(n, edges):
    # We follow a variant of Tarjan's algorithm here
    adjacentVertices = [[] for i in range(n)]

    # Populating arrays of neighbors
    for e in edges:
        adjacentVertices[e[0]].append(e[1])
        adjacentVertices[e[1]].append(e[0])

    # Variables needed for depth-first search
    vertexIndex = [-1 for i in range(n)] # Index assigned to vertex during search
    lowIndex = [-1 for i in range(n)]    # Index of lowest reachable vertex going forward in DFS
    prevVertex = [-1 for i in range(n)]  # Vertex which called the current vertex in DFS
    currentStack = []                    # Contains nodes in stack, for updating lowIndex purposes
    currentIndex = 0                     # Index to assign to next unvisited vertex
    criticalEdges = []                   # Return variable of the function
    initialVertex = 0                    # Determines where to start iteration
    callerVertex = -1                    # Vertex passed onto the next level of DFS

    # Note: we're not going to carry a visited array: a vertex is visited if its lowIndex
    # is equal to (-1) (a low index is assigned as soon as the vertex is visited.)

    def depthFirstSearch(i):
        nonlocal vertexIndex, lowIndex, currentStack, currentIndex, prevVertex
        nonlocal adjacentVertices, criticalEdges, initialVertex, n, edges

        vertexIndex[i] = currentIndex
        lowIndex[i] = currentIndex
        currentStack.append(i)
        currentIndex += 1

        while len(adjacentVertices[i]) > 0:
            # Take the next vertex that is adjacent to i
            nextVertex = adjacentVertices[i].pop()
            adjacentVertices[nextVertex].remove(i)

            # If vertex has not been visited, recurse to that vertex
            if (lowIndex[nextVertex] == -1):
                prevVertex[nextVertex] = i
                depthFirstSearch(nextVertex)

            # Once vertex has been visited, check whether lowIndex
            # needs to be updated

            if (nextVertex in currentStack) and (lowIndex[nextVertex] < lowIndex[i]):
                lowIndex[i] = lowIndex[nextVertex]

        if lowIndex[i] == vertexIndex[i]:
            # In this case, a critical edge has been found
            popVertex = currentStack.pop()
            lowIndex[popVertex] = lowIndex[i]
            while popVertex != i:
                popVertex = currentStack.pop()
                lowIndex[popVertex] = lowIndex[i]

            if prevVertex[i] >= 0:
                criticalEdges.append([i, prevVertex[i]])

    # Start iteration with vertex 0
    depthFirstSearch(0)

    return criticalEdges

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        return criticalConnections(n, connections)
