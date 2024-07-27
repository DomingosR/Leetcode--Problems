class Solution(object):
    def latestDayToCross(self, row, col, cells):
        numCells = row * col
        root = list(range(numCells + 2))
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        waterCells = set()
        
        def cellIndex(i, j):
            return col * (i - 1) + j
        
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                root[rootX] = rootY
        
        for k, cell in enumerate(cells):
            i, j = cell[0], cell[1]
            waterCells.add((i, j))
            currIndex = cellIndex(i, j)
            
            if j % col == 0:
                union(currIndex, numCells + 1)
                
            if j % col == 1:
                union(currIndex, 0)

            for dI, dJ in directions:
                newI, newJ = i + dI, j + dJ
                if row >= newI > 0 < newJ <= col and (newI, newJ) in waterCells:
                    union(currIndex, cellIndex(newI, newJ))
            
            if find(0) == find(numCells + 1):
                return k
        
        return len(cells)