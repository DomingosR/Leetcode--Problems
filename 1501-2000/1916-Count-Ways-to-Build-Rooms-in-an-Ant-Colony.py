class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        p = 10 ** 9 + 7
        
        children = defaultdict(list)
        for u in range(1, len(prevRoom)):
            children[prevRoom[u]].append(u)
            
        def numTopWays(u):
            if u not in children:
                return (1, 1)     # Total number of nodes in subtree, number of ways to sort them topologically
            
            numWays = 1
            n = 0
            
            for v in children[u]:
                nU, waysU = numTopWays(v)
                n += nU
                numWays = (numWays * waysU * comb(n, nU)) % p

            return (n + 1, numWays)
        
        return numTopWays(0)[1]