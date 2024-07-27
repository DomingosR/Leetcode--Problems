class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()
        parents = set()

        for parent, child, left in descriptions:
            children.add(child)
            parents.add(parent)
            
            if parent in nodes:
                pNode = nodes[parent]
            else:
                pNode = TreeNode(parent)
                nodes[parent] = pNode

            if child in nodes:
                cNode = nodes[child]
            else:
                cNode = TreeNode(child)
                nodes[child] = cNode

            if left:
                pNode.left = cNode
            else:
                pNode.right = cNode

        return nodes[list(parents - children)[0]]