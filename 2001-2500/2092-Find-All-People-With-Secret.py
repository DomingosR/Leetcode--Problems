class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        UFParent = list(range(n))
        UFRank = [1] * n
        
        def find(u):
            if UFParent[u] != u:
                UFParent[u] = find(UFParent[u])
            return UFParent[u]
        
        def union(u, v):
            u, v = min(u, v), max(u, v)
            rootU = UFParent[u]
            rootV = UFParent[v]
            if rootU == rootV:
                return False
            if UFRank[rootU] < UFRank[rootV]:
                rootU, rootV = rootV, rootU
            UFParent[rootV] = rootU
            UFRank[rootU] += UFRank[rootV]
            return True
            
        union(0, firstPerson)

        for t, meetingsPerTime in groupby(sorted(meetings, key = lambda x: x[2]), key = lambda x: x[2]):
            peopleSeen = set()
            for p1, p2, _ in meetingsPerTime: 
                peopleSeen.add(p1)
                peopleSeen.add(p2)
                union(p1, p2)
            
            for p in peopleSeen: 
                if find(p) != find(0):
                    UFParent[p] = p 
        
        return [u for u in range(n) if find(u) == find(0)]