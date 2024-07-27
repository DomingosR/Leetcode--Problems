class Solution(object):
    def maxNumOfSubstrings(self, s):
        charRange = defaultdict()
        for char in set(s):
            charRange[char] = (s.rindex(char), s.index(char))

        for char in set(s):
            auxLeft = -1
            auxRight = -1
            currentRight, currentLeft = charRange[char]
            while auxLeft != currentLeft or auxRight != currentRight:
                auxLeft, auxRight = currentLeft, currentRight
                currentLeft = min([charRange[auxChar][1] for auxChar in set(s[auxLeft:auxRight+1])])
                currentRight = max([charRange[auxChar][0] for auxChar in set(s[auxLeft:auxRight+1])])
            charRange[char] = (currentRight, currentLeft)

        substrings = []
        currentRight = -1
        for rightEnd, leftEnd in sorted(charRange.values()):
            if leftEnd > currentRight:
                substrings.append(s[leftEnd : rightEnd + 1])
                currentRight = rightEnd
        
        return substrings