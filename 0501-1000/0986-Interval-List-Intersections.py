class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []
        
        def intersect(int1, int2):
            a, b = int1
            c, d = int2
            
            return not (b < c or d < a)
        
        i, j, m, n = 0, 0, len(firstList), len(secondList)
        intersections = []   
        
        while i < m and j < n:
            int1, int2 = firstList[i], secondList[j]
            a, b = int1
            c, d = int2
            
            if intersect(int1, int2):
                intersections.append([max(a, c), min(b, d)])
                
            if b <= d:
                i += 1
            else:
                j += 1
                
        return intersections