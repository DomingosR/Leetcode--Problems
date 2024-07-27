class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        n, j, currCost, currMaxLen = len(s), -1, 0, 0
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        
        for i in range(n):
            currCost += cost[i]
            while j <= i and currCost > maxCost:
                j += 1
                currCost -= cost[j]
            currMaxLen = max(currMaxLen, i - j)
            
        return currMaxLen