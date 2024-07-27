class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        letters = "abcdefghijklmnopqrstuvwxyz"
        letterDict = {i:i for i in letters}
        
        def find(x):
            if letterDict[x] != x:
                letterDict[x] = find(letterDict[x])
            return letterDict[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if letterDict[rx] < letterDict[ry]:
                letterDict[ry] = rx
            else:
                letterDict[rx] = ry
        
        for char1, char2 in zip(s1, s2):
            union(char1, char2)
			
        ans = ''
        for s in baseStr:
            ans += find(s)
        return ans