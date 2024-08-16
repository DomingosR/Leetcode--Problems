class Solution(object):
    def rob(self, root):
        nodesProcessed = defaultdict(int)
        
        def processNode(node):
            if node not in nodesProcessed:
                if not node:
                    return 0

                val1 = node.val
                if node.left:
                    val1 += processNode(node.left.left) + processNode(node.left.right)
                if node.right:
                    val1 += processNode(node.right.left) + processNode(node.right.right)

                val2 = processNode(node.left) + processNode(node.right)

                nodesProcessed[node] = max(val1, val2)
            
            return nodesProcessed[node]
        
        return processNode(root)