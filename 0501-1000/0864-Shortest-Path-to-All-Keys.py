class Solution(object):
    def shortestPathAllKeys(self, grid):
        m = len(grid)
        n = len(grid[0])
        numKeys = 0
        keys = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
        locks = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        
        cellQueue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    cellQueue.appendleft((i, j, 0))
                elif grid[i][j] in keys:
                    numKeys += 1
        
        numSteps = 0
        visitedStates = set((i, j, 0))    
        
        while cellQueue:
            for _ in range(len(cellQueue)):
                i, j, keysFound = cellQueue.pop()
                
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if m > x >= 0 <= y < n:
                        currVal = grid[x][y]
                        
                        blocked = (currVal in locks and not (keysFound >> locks[currVal]) & 1) or currVal == '#'
                        if not blocked:
                            if currVal in keys:
                                newKeysFound = keysFound | (1 << keys[currVal])
                                if newKeysFound == (1 << numKeys) - 1:
                                    return numSteps + 1
                            else:
                                newKeysFound = keysFound

                            if (x, y, newKeysFound) not in visitedStates:
                                visitedStates.add((x, y, newKeysFound))
                                cellQueue.appendleft((x, y, newKeysFound))
            
            numSteps += 1

        return -1