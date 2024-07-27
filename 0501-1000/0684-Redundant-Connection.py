class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        UFAncestor = list(range(n+1))
        
        def find(v):
            while v != UFAncestor[v]:
                v = UFAncestor[v]
            return v
        
        def union(v, w):
            v, w = find(v), find(w)
            if v != w:
                UFAncestor[w] = v
                return True
            return False

        for v, w in edges:
            if not union(v, w):
                return [v, w]