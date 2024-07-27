class Solution(object):
    def distanceK(self, root, target, k):
        graphConnections = defaultdict(list)
        nodeQueue = deque()
        nodeQueue.appendleft(root)
        
        while nodeQueue:
            nextNode = nodeQueue.pop()
            if nextNode.left:
                graphConnections[nextNode.val].append(nextNode.left.val)
                graphConnections[nextNode.left.val].append(nextNode.val)                
                nodeQueue.appendleft(nextNode.left)
            if nextNode.right:
                graphConnections[nextNode.val].append(nextNode.right.val)
                graphConnections[nextNode.right.val].append(nextNode.val)                
                nodeQueue.appendleft(nextNode.right)
        
        valQueue = deque()
        valQueue.appendleft(target.val)
        seenValues = set()
        seenValues.add(target.val)
        
        for j in range(k):
            if valQueue:
                for i in range(len(valQueue)):
                    currentVal = valQueue.pop()
                    
                    for nextVal in graphConnections[currentVal]:
                        if nextVal not in seenValues:
                            valQueue.appendleft(nextVal)
                            seenValues.add(nextVal)
                            
        returnVal = []
        while valQueue:
            nextVal = valQueue.pop()
            returnVal.append(nextVal)
            
        return returnVal