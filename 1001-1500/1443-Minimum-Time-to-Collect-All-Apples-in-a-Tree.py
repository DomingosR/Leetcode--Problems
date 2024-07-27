class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if sum(hasApple) == 0:
            return 0
        
        numNodes = len(edges) + 1
        connectedNodes = defaultdict(list)

        for node1, node2 in edges:
            connectedNodes[node1].append(node2)
            connectedNodes[node2].append(node1)
        
        totalDist = 0

        def processVert(indVert):
            nonlocal totalDist

            subtreeHasApple = hasApple[indVert]

            for nextVert in connectedNodes[indVert]:
                print(indVert, nextVert, connectedNodes[indVert])
                connectedNodes[nextVert].remove(indVert)
                if processVert(nextVert):
                    subtreeHasApple = True
                    totalDist += 2
            
            connectedNodes[indVert] = []
            return subtreeHasApple

        processVert(0)

        return totalDist