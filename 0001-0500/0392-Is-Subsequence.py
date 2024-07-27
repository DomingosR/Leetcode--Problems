class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        
        if len(s) == 0:
            return True
        
        sPtr = 0
        for i in range(len(t)):
            if s[sPtr] == t[i]:
                sPtr += 1
            if sPtr == len(s):
                return True
        
        return sPtr == len(s)