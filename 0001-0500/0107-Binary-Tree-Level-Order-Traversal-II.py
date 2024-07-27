def binaryTreeReverseLevelOrderTraversal(root):
    if not root:
        return []
    
    # Main loop to produce arrays with levels
    queue = deque()
    queue.appendleft(root)
    treeValues = [root.val]
    treeLevels = [0]
    counter = 0

    while queue:
        currentNode = queue.pop()
        currentLevel = treeLevels[counter]

        if currentNode.left is not None:
            queue.appendleft(currentNode.left)
            treeValues.append(currentNode.left.val)
            treeLevels.append(currentLevel + 1)

        if currentNode.right is not None:
            queue.appendleft(currentNode.right)
            treeValues.append(currentNode.right.val)
            treeLevels.append(currentLevel + 1)

        counter += 1

    # Reformatting answer
    maxLevel = max(treeLevels)
    numNodes = len(treeValues)
    levelOrderTraversal = []

    for i in range(maxLevel, -1, -1):
        levelOrderTraversal.append([treeValues[j] for j in range(numNodes) if treeLevels[j] == i])

    return levelOrderTraversal

class Solution(object):
    def levelOrderBottom(self, root):
        return binaryTreeReverseLevelOrderTraversal(root)