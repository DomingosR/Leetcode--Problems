class Graph(object):

    def __init__(self, n, edges):
        self.numNodes = n
        self.allEdges = defaultdict(set)
        for currentNode, nextNode, cost in edges:
            self.allEdges[currentNode].add((cost, nextNode))

    def addEdge(self, edge):
        currentNode, nextNode, cost = edge
        self.allEdges[currentNode].add((cost, nextNode))

    def shortestPath(self, node1, node2):
        largeNum = (10**6 + 1) * self.numNodes
        minDist = [largeNum] * self.numNodes
        minDist[node1] = 0
        
        nodeHeap = []
        heapify(nodeHeap)
        heappush(nodeHeap, (0, node1))
            
        while nodeHeap:
            currentDist, currentNode = heappop(nodeHeap)
            if currentNode == node2:
                return currentDist
            if currentDist <= minDist[currentNode]:
                for edgeCost, nextNode in self.allEdges[currentNode]:
                    nextDist = currentDist + edgeCost
                    if nextDist < minDist[nextNode]:
                        minDist[nextNode] = nextDist
                        heappush(nodeHeap, (nextDist, nextNode))
                        
        return -1