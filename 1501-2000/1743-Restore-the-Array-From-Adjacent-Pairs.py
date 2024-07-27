class Solution(object):
    def restoreArray(self, adjacentPairs):
        adjacent = defaultdict(list)
        unpaired = set()
        
        def process(i):
            if i not in unpaired:
                unpaired.add(i)
            else:
                unpaired.remove(i)
                
        for i, j in adjacentPairs:
            adjacent[i].append(j)
            adjacent[j].append(i)
            process(i)
            process(j)
            
        start, end = list(unpaired)
        restored = [start]
        
        while restored[-1] != end:
            current = restored[-1]
            if len(restored) == 1 or adjacent[current][0] != restored[-2]:
                nextNum = adjacent[current][0]
            else:
                nextNum = adjacent[current][1]
            restored.append(nextNum)
        
        return restored