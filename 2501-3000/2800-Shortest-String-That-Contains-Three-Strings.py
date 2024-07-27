class Solution(object):
    def minimumString(self, a, b, c):
        def merge(s1, s2):
            if s1 in s2:
                return s2
            if s2 in s1:
                return s1
            
            n1, n2 = len(s1), len(s2)
            for i in range(n1, -1, -1):
                if s1[n1 - i:] == s2[:i]:
                    return s1 + s2[i:]
                
            return s1 + s2
        
        minLen = 1000
        minStr = ""
        
        for (x, y, z) in permutations((a, b, c)):
            combined = merge(merge(x, y), z)
            currLen = len(combined)
            if currLen < minLen or (currLen == minLen and combined <= minStr):
                minLen = currLen
                minStr = combined
                
        return minStr
        