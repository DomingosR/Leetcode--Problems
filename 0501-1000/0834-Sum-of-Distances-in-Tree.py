class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        countNodes = [1] * n
        sumDistances = [0] * n
        connectedNodes = defaultdict(list)

        for node1, node2 in edges:
            connectedNodes[node1].append(node2)
            connectedNodes[node2].append(node1)

        def countNodesInSubtree(node, previous):
            for nextNode in connectedNodes[node]:
                if nextNode != previous:
                    countNodesInSubtree(nextNode, node)
                    countNodes[node] += countNodes[nextNode]
                    sumDistances[node] += (sumDistances[nextNode] + countNodes[nextNode])
        
        def adjustSumDistances(node, previous):
            for nextNode in connectedNodes[node]:
                if nextNode != previous:
                    sumDistances[nextNode] = sumDistances[node] + (n - 2 * countNodes[nextNode])
                    adjustSumDistances(nextNode, node)
        
        countNodesInSubtree(0, -1)
        adjustSumDistances(0, -1)

        return sumDistances