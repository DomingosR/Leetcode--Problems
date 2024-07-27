class Solution(object):
    def minWindow(self, s, t):
        charsNeeded = Counter(t)
        charsMissing = len(t)
        start, end, i = 0, 0, 0
        
        for j, char in enumerate(s, 1):
            if charsNeeded[char] > 0:
                charsMissing -= 1
            charsNeeded[char] -= 1
            if charsMissing == 0:
                while i < j and charsNeeded[s[i]] < 0:
                    charsNeeded[s[i]] += 1
                    i += 1
                charsNeeded[s[i]] += 1
                charsMissing += 1
                if end == 0 or j - i < end - start:
                    start, end = i, j
                i += 1
        
        return s[start:end]