class Solution(object):
    def minCut(self, s):
        n = len(s)
        palindromes = [(n-i) for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:
                    palindromes[i] = min(palindromes[i], palindromes[j]+1)
        
        return palindromes[0] - 1