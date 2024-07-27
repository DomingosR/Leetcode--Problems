class Solution(object):
    def removeNodes(self, head):
        def processNode(node):
            if not node:
                return None
            node.next = processNode(node.next)
            if node.next and node.val < node.next.val:
                return node.next
            return node
        
        return processNode(head)