class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        graph = defaultdict(list)
        numEdges = len(edges)
        
        for i in range(numEdges):
            node1, node2 = edges[i]
            currProb = succProb[i]
            graph[node1].append((node2, currProb))
            graph[node2].append((node1, currProb))
            
        nodeQueue = deque()
        nodeQueue.appendleft(start)
        nodeProb = [0] * n
        nodeProb[start] = 1
        nodeSeen = [0] * n
        
        while nodeQueue:
            currNode = nodeQueue.pop()
            currProb = nodeProb[currNode]
            for nextNode, nextProb in graph[currNode]:
                if nextProb * currProb > nodeProb[nextNode]:
                    nodeProb[nextNode] = nextProb * currProb
                    nodeQueue.appendleft(nextNode)
        
        return nodeProb[end]