class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        maxLen = -1
        firstSeen = defaultdict(int)
        
        for i, c in enumerate(s):
            maxLen = max(maxLen, i - firstSeen.setdefault(c, i) - 1)
            
        return maxLen