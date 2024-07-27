class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = list(range(n))
        numProvinces = [n]

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootJ] = rootI
                numProvinces[0] -= 1

        for i in range(n-1):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return numProvinces[0]
