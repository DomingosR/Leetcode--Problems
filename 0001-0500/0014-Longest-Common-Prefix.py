class Solution(object):
    def longestCommonPrefix(self, strs):
        numStrings = len(strs)
        minLen = min([len(strs[i]) for i in range(numStrings)])

        if minLen == 0:
            return ""

        commonPrefix = ""
        i = 0

        while i < minLen:
            if len(Counter([strs[j][i] for j in range(numStrings)]).keys()) == 1:
                commonPrefix += strs[0][i]
                i += 1
            else:
                i = minLen
        
        return commonPrefix