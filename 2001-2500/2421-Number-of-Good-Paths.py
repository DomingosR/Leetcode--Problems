class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        n = len(vals)
        adjEdges = sorted([[max(vals[i], vals[j]), i, j] for i, j in edges])
        f = list(range(n))

        count = [Counter({vals[i]:1}) for i in range(n)]
        returnVal = n

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
            
        for v, i, j in adjEdges:
            findI, findJ = find(i), find(j)
            countJ, countI = count[findI][v], count[findJ][v]
            returnVal += countJ * countI
            f[findJ] = findI
            count[findI] = Counter({v: countJ + countI})

        return returnVal