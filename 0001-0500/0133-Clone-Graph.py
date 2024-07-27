class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        
        clonedNodes = defaultdict(Node)
        newNode = Node(node.val)
        clonedNodes[node] = newNode
        
        nodeQueue = deque()
        nodeQueue.appendleft(node)
        
        while nodeQueue:
            currentNode = nodeQueue.pop()
            currentCloned = clonedNodes[currentNode]
            for nextNode in currentNode.neighbors:
                if nextNode not in clonedNodes:
                    nodeQueue.appendleft(nextNode)
                    auxNode = Node(nextNode.val)
                    clonedNodes[nextNode] = auxNode
                currentCloned.neighbors.append(clonedNodes[nextNode])
                
        return newNode