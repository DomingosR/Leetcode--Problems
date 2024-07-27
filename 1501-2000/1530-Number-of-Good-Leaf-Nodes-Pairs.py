class Solution(object):
    def countPairs(self, root, distance):
        numPairs = [0]
        
        def processNode(node):
            if not (node.left or node.right):
                return (Counter({0: 1}), 0)
            
            if node.left:
                counterLeft, numLeft = processNode(node.left)
                
            if node.right:
                counterRight, numRight = processNode(node.right)
                
            if node.left and node.right:
                numPairs = numLeft + numRight
                for vL in counterLeft:
                    for vR in counterRight:
                        if vL + vR + 2 <= distance:
                            numPairs += counterLeft[vL] * counterRight[vR]
                
                newCounter = Counter()
                for v in set(counterLeft) | set(counterRight):
                    newCounter[v+1] = counterLeft[v] + counterRight[v]
            
            elif node.left:
                numPairs = numLeft
                newCounter = Counter()
                for v in set(counterLeft):
                    newCounter[v+1] = counterLeft[v]
                    
            else:
                numPairs = numRight
                newCounter = Counter()
                for v in set(counterRight):
                    newCounter[v+1] = counterRight[v] 
            
            return (newCounter, numPairs)
        
        return processNode(root)[1]