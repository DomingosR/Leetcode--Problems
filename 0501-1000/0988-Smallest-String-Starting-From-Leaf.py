class Solution(object):
    def smallestFromLeaf(self, root):
        minStr = "{"    # Any string which is lexicographically > "z" will do here
        nodeQueue = deque()
        nodeQueue.appendleft((root, ""))

        while nodeQueue:
            currNode, currStr = nodeQueue.pop()
            currStr = chr(currNode.val + 97) + currStr
            if not (currNode.left or currNode.right):
                minStr = currStr if (currStr < minStr) else minStr
            else:
                if currNode.left:
                    nodeQueue.appendleft((currNode.left, currStr))
                if currNode.right:
                    nodeQueue.appendleft((currNode.right, currStr))

        return minStr
