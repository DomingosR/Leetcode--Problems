class unionFind:
    def __init__(self, n):
        self.count = n
        self.rank = [0] * n
        self.parent = list(range(n))
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        parentI = self.find(i)
        parentJ = self.find(j)
        
        if parentI == parentJ:
            return False
        
        rankI = self.rank[parentI]
        rankJ = self.rank[parentJ]
        
        if rankI < rankJ:
            rankI, rankJ, parentI, parentJ = rankJ, rankI, parentJ, parentI
        
        self.parent[parentJ] = self.parent[parentI]
        if rankI == rankJ:
            self.rank[parentI] += 1
        
        self.count -= 1
        return True

class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        adjEdges = sorted([(w, i, j) for i, j, w in edgeList])
        adjQueries = sorted([(limit, p, q, queryNo) for queryNo, (p, q, limit) in enumerate(queries)])
        uf = unionFind(n)
        returnVal = [False] * len(queries)
        
        s = 0
        for limit, p, q, queryNo in adjQueries:
            while s < len(edgeList) and adjEdges[s][0] < limit:
                w, i, j = adjEdges[s]
                uf.union(i, j)
                s += 1
            returnVal[queryNo] = (uf.find(p) == uf.find(q))
        
        return returnVal