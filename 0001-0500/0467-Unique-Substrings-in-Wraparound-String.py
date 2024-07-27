class Solution(object):
    def findSubstringInWraproundString(self, p):
        # The contribution of each letter is the number of unique substrings
        # of base ending in that letter in p.  The dictionary below keeps
        # track of that contribution.

        letterContribution = {letter: 1 for letter in p}

        currentLen = 1
        for i in range(len(p) - 1):
            currentLen = (currentLen + 1) if (ord(p[i+1]) - ord(p[i])) % 26 == 1 else 1
            letterContribution[p[i+1]] = max(letterContribution[p[i+1]], currentLen)

        return sum(letterContribution.values())
