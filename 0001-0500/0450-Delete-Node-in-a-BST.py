class Solution(object):
    def deleteNode(self, root, key):
        def processNode(node, target):
            if not node:
                return None

            if node.val == target:
                if not node.left:
                    return node.right

                if not node.right:
                    return node.left

                if node.left and node.right:
                    auxNode = node.right
                    while auxNode.left:
                        auxNode = auxNode.left

                    node.val = auxNode.val
                    node.right = processNode(node.right, node.val)

            elif node.val > target:
                node.left = processNode(node.left, target)

            else:
                node.right = processNode(node.right, target)

            return node

        return processNode(root, key)
