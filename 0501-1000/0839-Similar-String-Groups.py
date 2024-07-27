class Solution(object):
    def numSimilarGroups(self, strs):
        n = len(strs[0])
        numStrs = len(strs)
        unionFind = {}
        ranks = defaultdict(int)
        
        def find(x):
            if x not in unionFind:
                unionFind[x] = x
            if x != unionFind[x]:
                unionFind[x] = find(unionFind[x])
            return unionFind[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if ranks[rootX] < ranks[rootY]:
                unionFind[rootX] = rootY
            else:
                unionFind[rootY] = rootX
                if ranks[rootX] == ranks[rootY]:
                    ranks[rootX] += 1
            
        def similarStrings(str1, str2):
            diffCount = len([i for i in range(n) if str1[i] != str2[i]])
            return diffCount == 0 or diffCount == 2
        
        for i in range(numStrs):
            for j in range(i + 1, numStrs):
                if similarStrings(strs[i], strs[j]):
                    union(strs[i], strs[j])
        
        return len(set([find(x) for x in strs]))