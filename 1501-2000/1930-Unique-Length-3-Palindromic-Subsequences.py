class Solution(object):
    def countPalindromicSubsequence(self, s):
        numPalindromes = 0
        
        for indChar in string.ascii_lowercase:
            start, end = s.find(indChar), s.rfind(indChar)
            if start < end:
                numPalindromes += len(set(s[start + 1 : end]))
            
        return numPalindromes