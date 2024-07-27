from collections import defaultdict, Counter

def validPath(inputPairs):
    # Storing graph info
    graphInfo = defaultdict(list)
    numIn = Counter()
    numOut = Counter()

    for u, v in inputPairs:
        graphInfo[u].append(v)
        numIn[v] += 1
        numOut[u] += 1

    # Determining starting point, which is a vertex with more outgoing than
    # incoming edges if it exists, and arbitrary otherwise
    start = inputPairs[0][0]
    for u in numOut:
        if numOut[u] > numIn[u]:
            start = u
            break
    
    # Using Hierholzer's algorithm to compute route
    finalRoute = []
    vertexStack = [start]

    while vertexStack:
        while graphInfo[vertexStack[-1]]:
            vertexStack.append(graphInfo[vertexStack[-1]].pop())
        finalRoute.append(vertexStack.pop())
    finalRoute.reverse()

    return [[finalRoute[i], finalRoute[i+1]] for i in range(len(finalRoute) - 1)]

class Solution(object):
    def validArrangement(self, pairs):
        return validPath(pairs)