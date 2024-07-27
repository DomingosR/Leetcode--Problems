class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        nodeQueue = deque()
        nodeQueue.appendleft(root)
        zigZagTraversal = []
        reversed = False

        while nodeQueue:
            zigZagTraversal.append([])
            for i in range(len(nodeQueue)):
                nextNode = nodeQueue.pop()
                if reversed:
                    zigZagTraversal[-1].insert(0, nextNode.val)
                else:
                    zigZagTraversal[-1].append(nextNode.val)
                if nextNode.left:
                    nodeQueue.appendleft(nextNode.left)
                if nextNode.right:
                    nodeQueue.appendleft(nextNode.right)
            reversed = not reversed
        
        # return [(zigZagTraversal[i][::-1] if i % 2 == 1 else zigZagTraversal[i]) \
        #        for i in range(len(zigZagTraversal))]
        return zigZagTraversal