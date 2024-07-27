class Solution(object):
    def flatten(self, root):
        if root:
            currentNode = root

            while currentNode.left or currentNode.right:
                if currentNode.left:
                    finalRightNode = currentNode.left
                    while finalRightNode.right:
                        finalRightNode = finalRightNode.right
                    finalRightNode.right = currentNode.right
                    currentNode.right = currentNode.left
                    currentNode.left = None
                currentNode = currentNode.right