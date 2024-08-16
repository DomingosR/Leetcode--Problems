class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        vertexQueue = deque([(1, 0)])
        numEdgesVisited = defaultdict(list)
        numEdgesVisited[1] = [0, -1]
        
        while vertexQueue:
            if n in numEdgesVisited and numEdgesVisited[n][1] > 0:
                break    
            u, count = vertexQueue.pop()
            for v in neighbors[u]:    
                if v not in numEdgesVisited:
                    numEdgesVisited[v] = [count + 1, -1]
                    vertexQueue.appendleft((v, count + 1))    
                elif numEdgesVisited[v][-1] > 0:
                    continue    
                elif count == numEdgesVisited[v][0]:
                    numEdgesVisited[v][-1] = count + 1
                    vertexQueue.appendleft((v, count + 1))
            
        finalNumEdges = numEdgesVisited[n][1] if numEdgesVisited[n][1] > 0 else numEdgesVisited[n][0] + 2 
        
        timeElapsed = 0
        for edgeCounter in range(finalNumEdges):
            timeElapsed += time
            if edgeCounter < finalNumEdges - 1 and (timeElapsed // change) % 2:
                timeElapsed += change - (timeElapsed % change)
                
        return timeElapsed