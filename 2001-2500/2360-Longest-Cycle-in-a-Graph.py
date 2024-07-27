class Solution(object):
    def longestCycle(self, edges):
        n = len(edges)
        cycleLen = -1
        timeVisited = [0] * n 
        startTime = 1

        for v in range(n):
            if timeVisited[v] == 0:
                currentTime = startTime
                currentVertex = v
                while currentVertex != -1 and timeVisited[currentVertex] == 0:
                    timeVisited[currentVertex] = currentTime
                    currentTime += 1
                    currentVertex = edges[currentVertex]
                if currentVertex != -1 and timeVisited[currentVertex] >= startTime:
                    cycleLen = max(cycleLen, currentTime - timeVisited[currentVertex])
                startTime = currentTime + 1
        
        return cycleLen
