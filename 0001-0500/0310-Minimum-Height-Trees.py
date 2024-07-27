class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        neighbors = defaultdict(set)
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        currentVertices = [u for u in range(n) if len(neighbors[u]) == 1]

        while n > 2:
            n -= len(currentVertices)
            nextVertices = []

            for u in currentVertices:
                v = neighbors[u].pop()
                neighbors[v].remove(u)
                if len(neighbors[v]) == 1:
                    nextVertices.append(v)

            currentVertices = nextVertices

        return currentVertices
