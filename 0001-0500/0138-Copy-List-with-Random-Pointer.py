class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        
        clonedNodes = defaultdict(Node)
        newHead = Node(head.val)
        clonedNodes[head] = newHead
        
        currentNode = head
        
        while currentNode:
            currentNext = currentNode.next
            currentRandom = currentNode.random
            clonedNode = clonedNodes[currentNode]
            
            if currentNext:
                if currentNext not in clonedNodes:
                    clonedNodes[currentNext] = Node(currentNext.val)
                clonedNext = clonedNodes[currentNext]
                clonedNode.next = clonedNext
            
            if currentRandom:
                if currentRandom not in clonedNodes:
                    clonedNodes[currentRandom] = Node(currentRandom.val)
                clonedRandom = clonedNodes[currentRandom]
                clonedNode.random = clonedRandom
                
            currentNode = currentNext
                
        return newHead