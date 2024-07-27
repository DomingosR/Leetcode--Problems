class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        UFAncestor = list(range(n+1))
        numParents = [0] * (n+1)
        hasMultiple = 0

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

        def unionFind():
            for v, w in edges:
                if not union(v, w):
                    return [v, w]
            return None

        for v, w in edges:
            numParents[w] += 1
            if numParents[w] == 2:
                hasMultiple = w

        if hasMultiple:
            candidates = [[v, w] for v, w in edges if w == hasMultiple]
            edges.remove(candidates[1])
            if not unionFind():
                return candidates[1]
            return candidates[0]
        else:
            return unionFind()