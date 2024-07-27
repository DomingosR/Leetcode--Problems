class Solution(object):
    def isIsomorphic(self, s, t):
        dictS = dict()
        dictT = dict()
        
        for i in range(len(s)):
            if (s[i] in dictS) ^ (t[i] in dictT):
                return False
            
            if (s[i] in dictS) and (t[i] in dictT):
                if dictS[s[i]] != dictT[t[i]]:
                    return False
            else:
                dictS[s[i]] = i
                dictT[t[i]] = i
                
        return True