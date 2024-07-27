class Solution(object):
    def maximumImportance(self, n, roads):
        roadCount = [0] * n
        
        for city1, city2 in roads:
            roadCount[city1] += 1
            roadCount[city2] += 1
            
        roadCount.sort()
        
        return sum([(i+1) * roadCount[i] for i in range(n)])