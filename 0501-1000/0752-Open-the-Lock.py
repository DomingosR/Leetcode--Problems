class Solution(object):
    def openLock(self, deadends, target):
        if target == "0000":
            return 0
        
        deadEnds = set(deadends)
        if "0000" in deadEnds:
            return -1
        
        visited = set("0000")
        combinationQueue = deque()
        combinationQueue.appendleft(("0000", 0))
        
        while combinationQueue:
            currentComb, currNumMoves = combinationQueue.pop()
            
            for i in range(4):
                currDigit = int(currentComb[i])
                for delta in [-1, 1]:
                    nextDigit = (currDigit + delta) % 10
                    newComb = currentComb[:i] + str(nextDigit) + currentComb[i+1:]
                    
                    if newComb == target:
                        return currNumMoves + 1
                                          
                    if (newComb not in deadEnds) and (newComb not in visited):
                        visited.add(newComb)
                        combinationQueue.appendleft((newComb, currNumMoves + 1))
        
        return -1