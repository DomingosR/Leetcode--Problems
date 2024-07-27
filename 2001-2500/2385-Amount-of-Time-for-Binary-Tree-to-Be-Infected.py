class Solution(object):
    def amountOfTime(self, root, start):
        vertexQueue = deque([root])
        neighbors = defaultdict(set)
        
        while vertexQueue:
            currVertex = vertexQueue.pop()
            if currVertex.left:
                neighbors[currVertex.val].add(currVertex.left.val)
                neighbors[currVertex.left.val].add(currVertex.val)
                vertexQueue.appendleft(currVertex.left)
            if currVertex.right:
                neighbors[currVertex.val].add(currVertex.right.val)
                neighbors[currVertex.right.val].add(currVertex.val)
                vertexQueue.appendleft(currVertex.right)
                
        numQueue = deque([(start, 0)])
        seenNums = set([start])        
        
        while numQueue:
            currNum, currLevel = numQueue.pop()
            for nextNum in neighbors[currNum]:
                if nextNum not in seenNums:
                    numQueue.appendleft((nextNum, currLevel + 1))
                    seenNums.add(nextNum)
                    
        return currLevel