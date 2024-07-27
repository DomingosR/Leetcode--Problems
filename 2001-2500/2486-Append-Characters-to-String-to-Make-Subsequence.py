class Solution(object):
    def appendCharacters(self, s, t):
        lenS, lenT = len(s), len(t)
        iS, iT = 0, 0
        
        while iT < lenT:
            while iS < lenS and t[iT] != s[iS]:
                iS += 1
            if iS < lenS:
                iT += 1
                iS += 1
            if iS == lenS:
                return lenT - iT
            
        return lenT - iT