class Solution(object):
    def countSubTrees(self, n, edges, labels):
        subtreeCount = [0] * n

        connectedNodes = defaultdict(list)
        for node1, node2 in edges:
            connectedNodes[node1].append(node2)
            connectedNodes[node2].append(node1)
        
        def dfs(currentNode, parentNode):
            currentCount = Counter(labels[currentNode])
            for childNode in connectedNodes[currentNode]:
                if childNode != parentNode:
                    currentCount += dfs(childNode, currentNode)
            subtreeCount[currentNode] = currentCount[labels[currentNode]]
            return currentCount
        
        dfs(0, -1)
        return subtreeCount