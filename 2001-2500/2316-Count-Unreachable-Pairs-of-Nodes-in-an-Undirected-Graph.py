class Solution(object):
    def countPairs(self, n, edges):
        root = [i for i in range(n)]
        rank = [1] * n

        def find(i):
            if root[i] == i:
                return i
            root[i] = find(root[i])
            return root[i]
        
        def union(i, j):
            rootI = find(i)
            rootJ = find(j)

            if rootI != rootJ:
                if rank[rootI] > rank[rootJ]:
                    root[rootJ] = rootI
                elif rank[rootI] < rank[rootJ]:
                    root[rootI] = rootJ
                else:
                    root[rootJ] = rootI
                    rank[rootI] += 1

        for i, j in edges:
            union(i, j)
        
        roots = [find(i) for i in range(n)]
        valCounter = Counter(roots)
        values = [k for k in valCounter.values()]

        numPairs = 0
        currentSum = values[0]
        for l in range(1, len(values)):
            numPairs += currentSum * values[l]
            currentSum += values[l]

        return numPairs