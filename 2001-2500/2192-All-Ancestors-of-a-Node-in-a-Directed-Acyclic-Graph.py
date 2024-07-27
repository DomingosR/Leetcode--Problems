class Solution(object):
    def getAncestors(self, n, edges):
        ancestors = defaultdict(set)
        processed = set()
        
        for u, v in edges:
            ancestors[v].add(u)

        def process(u):
            if u not in processed:
                processed.add(u)
                auxSet = set()
                for v in ancestors[u]:
                    process(v)
                    auxSet |= ancestors[v]
                ancestors[u] |= auxSet

        for u in range(n):
            process(u)

        return [sorted(list(ancestors[u])) for u in range(n)]