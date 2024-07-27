class Solution:
    def largestPathValue(self, colors, edges):
        numNodes = len(colors)
        incomingCount = [0] * numNodes
        graphEdges = [[] for i in range(numNodes)]

        for v1, v2 in edges:
            incomingCount[v2] += 1
            graphEdges[v1].append(v2)

        stack = [v for v in range(numNodes) if incomingCount[v] == 0]
        colorCount = [[0] * 26 for i in range(numNodes)]

        while stack:
            v1 = stack.pop()
            colorCount[v1][ord(colors[v1]) - ord('a')] += 1
            for v2 in graphEdges[v1]:
                colorCount[v2] = list(map(max, colorCount[v2], colorCount[v1]))
                incomingCount[v2] -= 1
                if incomingCount[v2] == 0:
                    stack.append(v2)

        return -1 if sum(incomingCount) > 0 else max([max(count) for count in colorCount])