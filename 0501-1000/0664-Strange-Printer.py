class Solution(object):
    def strangePrinter(self, s):
        s1 = s[0]
        
        for i in range(1, len(s)):
            if s[i] != s1[-1]:
                s1 += s[i]
        
        preComputed = {}
        
        def dp(i, j):
            if i > j: 
                return 0
            
            if (i, j) not in preComputed:
                returnVal = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s1[k] == s1[i]:
                        returnVal = min(returnVal, dp(i, k-1) + dp(k+1, j))
                        
                preComputed[(i, j)] = returnVal
            
            return preComputed[(i, j)]
        
        return dp(0, len(s1) - 1)