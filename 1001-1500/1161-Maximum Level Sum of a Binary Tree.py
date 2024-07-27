class Solution(object):
    def maxLevelSum(self, root):
        nodeQueue = deque()

        maxLevel = 1
        maxLevelSum = root.val
        currentLevel = 2

        if root.left: 
            nodeQueue.appendleft(root.left)
        if root.right:
            nodeQueue.appendleft(root.right)

        while nodeQueue:
            currentLevelSum = 0

            for _ in range(len(nodeQueue)):
                currentNode = nodeQueue.pop()
                currentLevelSum += currentNode.val
                if currentNode.left:
                    nodeQueue.appendleft(currentNode.left)
                if currentNode.right:
                    nodeQueue.appendleft(currentNode.right)
            
            if currentLevelSum > maxLevelSum:
                maxLevel = currentLevel
                maxLevelSum = currentLevelSum
            
            currentLevel += 1
        
        return maxLevel