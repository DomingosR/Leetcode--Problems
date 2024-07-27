class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):    
        def buildGraph(conditions):
            numPredecessors = defaultdict(int)
            successors = defaultdict(list)
            
            for v1, v2 in conditions:
                numPredecessors[v2] += 1
                successors[v1].append(v2)
            
            vertexQueue = deque([v for v in range(1, k+1) if numPredecessors[v] == 0])
            finalOrder = []
            
            while vertexQueue:
                v1 = vertexQueue.pop()
                finalOrder.append(v1)
                
                for v2 in successors[v1]:
                    numPredecessors[v2] -= 1
                    if numPredecessors[v2] == 0:
                        vertexQueue.appendleft(v2)
        
            return [] if len(finalOrder) < k else finalOrder
        
        orderRow = buildGraph(rowConditions)
        orderCol = buildGraph(colConditions)
        
        if not (orderRow and orderCol):
            return []

        finalMatrix = [[0] * k for _ in range(k)]
        for i in range(k):
            val = orderRow[i]
            finalMatrix[i][orderCol.index(val)] = val
            
        return finalMatrix