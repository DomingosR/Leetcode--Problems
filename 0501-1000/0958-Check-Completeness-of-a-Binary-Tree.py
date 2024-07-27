class Solution(object):
    def isCompleteTree(self, root):
        nodes = deque()
        nodes.appendleft(root)
        emptyNodeFound = [False]

        def processNode(node):
            if node and emptyNodeFound[0]:
                return False

            if node:
                nodes.appendleft(node)
            else:
                emptyNodeFound[0] = True

            return True

        while nodes:
            nextNode = nodes.pop()
            if not processNode(nextNode.left): return False
            if not processNode(nextNode.right): return False

        return True
