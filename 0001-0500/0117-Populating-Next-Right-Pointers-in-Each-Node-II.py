from collections import deque

def createNextPointers(root):
    if root is None:
        return None

    def findNextNode(inputNode, parentNode):
        if parentNode == None:
            return None
        if parentNode.right != None and parentNode.right != inputNode:
            return parentNode.right
        else:
            currentNode = parentNode
            nextFound = False
            while currentNode.next != None:
                currentNode = currentNode.next
                if currentNode.left != None:
                    return currentNode.left
                elif currentNode.right != None:
                    return currentNode.right
            return None
    
    queue = deque([])
    queue.appendleft([root, None])
    
    while queue:
        newPair = queue.pop()
        currentNode = newPair[0]
        parentNode = newPair[1]
        currentNode.next = findNextNode(currentNode, parentNode)
        if currentNode.left != None:
            queue.appendleft([currentNode.left, currentNode])
        if currentNode.right != None:
            queue.appendleft([currentNode.right, currentNode])
            
    return root

class Solution(object):
    def connect(self, root):
        return createNextPointers(root)