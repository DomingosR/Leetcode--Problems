class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        
        n = len(haystack)
        for i in range(n - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1