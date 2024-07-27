class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 2:
            return trees
            
        points = [(p[0], p[1]) for p in trees]
        sortedPoints = sorted(set(points))
        
        def crossProduct(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
        
        lowerHull = []
        for p in sortedPoints:
            while len(lowerHull) >= 2 and crossProduct(lowerHull[-2], lowerHull[-1], p) < 0:
                lowerHull.pop()
            lowerHull.append(p)
            
        upperHull = []

        for p in reversed(sortedPoints):
            while len(upperHull) >= 2 and crossProduct(upperHull[-2], upperHull[-1], p) < 0:
                upperHull.pop()
            upperHull.append(p)   
            
        return list(set(lowerHull[:-1] + upperHull[:-1]))