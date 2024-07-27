class Solution(object):
    def sortedListToBST(self, head):
        def processNode(startNode):
            if not startNode:
                return None
            if not startNode.next:
                return TreeNode(startNode.val)

            slowPtr, fastPtr = startNode, startNode.next
            while fastPtr.next and fastPtr.next.next:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next
            
            nextRoot = TreeNode(slowPtr.next.val)

            startLeft = startNode
            startRight = slowPtr.next.next
            slowPtr.next = None

            nextRoot.left = processNode(startLeft)
            nextRoot.right = processNode(startRight)

            return nextRoot

        return processNode(head)