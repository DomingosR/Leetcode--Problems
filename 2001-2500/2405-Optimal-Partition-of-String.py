class Solution(object):
    def partitionString(self, s):
        n = len(s)
        
        lastSeen = defaultdict()
        lastSeen[s[0]] = 0
        numStrings = 1
        currentStart = 0

        for i in range(1, n):
            if s[i] in lastSeen.keys() and lastSeen[s[i]] >= currentStart:
                numStrings += 1
                currentStart = i
            lastSeen[s[i]] = i

        return numStrings