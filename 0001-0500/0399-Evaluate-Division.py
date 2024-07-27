class Solution(object):
    def calcEquation(self, equations, values, queries):
        graphEdges = {}

        def buildGraph(equations, values):
            def addEdge(v1, v2, val):
                if v1 in graphEdges:
                    graphEdges[v1].append((v2, val))
                else:
                    graphEdges[v1] = [(v2, val)]

            for vertices, val in zip(equations, values):
                v1, v2 = vertices
                addEdge(v1, v2, val)
                addEdge(v2, v1, 1.0 / val)

        def getEquationVal(query):
            v1, v2 = query
            if v1 not in graphEdges or v2 not in graphEdges:
                return -1.0

            queue = collections.deque([(v1, 1.0)])
            visited = set()

            while queue:
                auxVert, productVal = queue.pop()
                if auxVert == v2:
                    return productVal

                visited.add(auxVert)
                for auxVert2, edgeVal in graphEdges[auxVert]:
                    if auxVert2 not in visited:
                        queue.appendleft((auxVert2, productVal * edgeVal))

            return -1.0

        buildGraph(equations, values)
        return [getEquationVal(query) for query in queries]
