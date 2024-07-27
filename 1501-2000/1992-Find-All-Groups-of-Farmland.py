class Solution(object):
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        farmland = []

        def process(i, j):
            i1, j1 = i, j
            while i1 < m - 1 and land[i1 + 1][j] == 1:
                i1 += 1
            while j1 < n - 1 and land[i1][j1 + 1] == 1:
                j1 += 1
            
            for i2 in range(i, i1 + 1):
                for j2 in range(j, j1 + 1):
                    land[i2][j2] = 0

            return [i, j, i1, j1]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    farmland.append(process(i, j))

        return farmland