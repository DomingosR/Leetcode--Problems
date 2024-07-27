class Solution(object):
    def mergeNodes(self, head):
        currValNode = None
        currListNode = head
        
        while currListNode.next:
            value = 0
            while currListNode.next.val != 0:
                currListNode = currListNode.next
                value += currListNode.val
            currValNode = currValNode.next if currValNode else head
            currValNode.val = value
            currListNode = currListNode.next
            
        currValNode.next = None
        return head