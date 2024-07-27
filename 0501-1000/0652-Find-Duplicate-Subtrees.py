class Solution(object):
    def findDuplicateSubtrees(self, root):
        # Dictionary to contain the root nodes of each subtree
        # with a particular structure
        nodesForStruct = defaultdict(list)

        # Function to traverse a particular node in the tree
        # constructing the structure of the tree
        def traverse(node):
            if not node:
                return "Null"
            returnVal = "%s, %s, %s" % (str(node.val), traverse(node.left), traverse(node.right))
            nodesForStruct[returnVal].append(node)
            return returnVal
        
        # Traverse the tree to construct nodesForStruct
        traverse(root)
        
        return [nodesForStruct[indStruct][0] for indStruct in nodesForStruct if len(nodesForStruct[indStruct]) > 1]