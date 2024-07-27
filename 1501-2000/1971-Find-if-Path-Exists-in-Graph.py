class Solution(object):
    def validPath(self, n, edges, source, destination):
        UFRoot = list(range(n))

        def find(u):
            if UFRoot[u]!= u:
                UFRoot[u] = find(UFRoot[u])
            return UFRoot[u]

        def union(u, v):
            u, v = find(u), find(v)
            if u == v:
                return False
            UFRoot[v] = u
            return True

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
