class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edgesAlice = [[u-1, v-1] for [t, u, v] in edges if t == 1]  
        edgesBob   = [[u-1, v-1] for [t, u, v] in edges if t == 2]  
        edgesBoth  = [[u-1, v-1] for [t, u, v] in edges if t == 3]
        nAlice, nBob = len(edgesAlice), len(edgesBob)
        
        # Union-Find code
        UFParent = list(range(n))
        
        def find(u):
            if u != UFParent[u]:
                UFParent[u] = find(UFParent[u])
            return UFParent[u]
        
        def union(u, v):
            u, v = find(u), find(v)
            if u != v:
                UFParent[v] = u
                return True
            return False
        
        # Process edges for both
        components = n
        removed = 0
        
        for u, v in edgesBoth:
            if union(u, v):
                components -= 1
            else:
                removed += 1
        
        # If both can traverse graph, remove all individual edges
        if components == 1:
            return nAlice + nBob + removed
        
        # Process edges for each separately, save information for later processing
        UFParentAux, componentsAux = UFParent.copy(), components
        
        # Process edges for Alice
        for u, v in edgesAlice:
            if union(u, v):
                components -= 1
            else:
                removed += 1
                
        if components > 1:
            return -1
        
        # Restore information, then process edges for Bob
        UFParent, components = UFParentAux, componentsAux
        
        for u, v in edgesBob:
            if union(u, v):
                components -= 1
            else:
                removed += 1
        
        return -1 if components > 1 else removed  