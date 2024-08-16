class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ")" or grid[-1][-1] == "(":
            return False
        
        possibleNetOpen = defaultdict(set)
        possibleNetOpen[(-1, 0)] = {0}
        possibleNetOpen[(0, -1)] = {0}
        
        for i in range(m):
            for j in range(n):
                toAdd = 1 if grid[i][j] == "(" else -1
                possibleNetOpen[(i, j)] = {current + toAdd \
                        for current in possibleNetOpen[(i, j-1)] | possibleNetOpen[(i-1, j)] \
                        if current + toAdd >= 0}
        
        return 0 in possibleNetOpen[(m-1, n-1)]