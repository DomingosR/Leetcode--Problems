class Solution(object):
    def groupThePeople(self, groupSizes):
        n = len(groupSizes)
        idsPerSize = defaultdict(list)
        
        for i in range(n):
            idsPerSize[groupSizes[i]].append(i)
        
        finalGroups = []
        
        for size in idsPerSize:
            m = len(idsPerSize[size])
            i = 0
            while i < m:
                finalGroups.append(idsPerSize[size][i:i+size])
                i += size
        
        return finalGroups