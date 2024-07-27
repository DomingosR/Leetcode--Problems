def binaryTreeLevelOrderTraversal(root):
    if not root:
        return []
    
    # Main loop to produce arrays with levels
    queue = deque()
    queue.appendleft(root)
    treeArray = [root.val]
    treeLevels = [0]
    counter = 0

    while queue:
        currentNode = queue.pop()
        currentLevel = treeLevels[counter]

        if not currentNode.left is None:
            queue.appendleft(currentNode.left)
            treeArray.append(currentNode.left.val)
            treeLevels.append(currentLevel + 1)

        if not currentNode.right is None:
            queue.appendleft(currentNode.right)
            treeArray.append(currentNode.right.val)
            treeLevels.append(currentLevel + 1)

        counter += 1

    # Reformatting answer
    maxLevel = max(treeLevels)
    numNodes = len(treeArray)
    levelOrderTraversal = []

    for i in range(maxLevel + 1):
        levelOrderTraversal.append([treeArray[j] for j in range(numNodes) if treeLevels[j] == i])

    return levelOrderTraversal

class Solution(object):
    def levelOrder(self, root):
        return binaryTreeLevelOrderTraversal(root)