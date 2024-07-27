class Solution(object):
    def checkWays(self, pairs):
        related = defaultdict(set)
        allVertices = set()
        for u, v in pairs:
            allVertices.add(u)
            allVertices.add(v)
            related[u].add(v)
            related[v].add(u)
            
        def numTrees(vertexSet):
            n = len(vertexSet)
            if len(vertexSet) <= 1:
                return 1

            verticesByCount = defaultdict(set)

            for u in vertexSet:
                relatedCount = 0
                for v in related[u]:
                    if v in vertexSet:
                        relatedCount += 1

                verticesByCount[relatedCount].add(u)
                
            if len(verticesByCount[n-1]) == 0:
                return 0

            isUnique = False if len(verticesByCount[n-1]) >= 2 else True
            otherVertices = vertexSet - verticesByCount[n-1]

            if len(otherVertices) > 0:
                seenVertices = set()
                relatedInSet = defaultdict(set)

                for u in otherVertices:
                    if u not in seenVertices:
                        seenVertices.add(u)
                        relatedInSet[u].add(u)
                        vertexQueue = deque()
                        vertexQueue.appendleft(u)
                        while vertexQueue:
                            v = vertexQueue.pop()
                            for w in related[v]:
                                if w in otherVertices and w not in seenVertices:
                                    relatedInSet[u].add(w)
                                    seenVertices.add(w)
                                    vertexQueue.appendleft(w)

                for currentSet in relatedInSet.values():
                    currentNum = numTrees(currentSet)
                    if currentNum == 0:
                        return 0
                    if currentNum >= 2:
                        isUnique = False

            return 1 if isUnique else 2
        
        return numTrees(allVertices)