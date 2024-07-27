class Solution(object):
    def partition(self, s):
        n = len(s)
        palindromes = [[] for _ in range(n+1)]
        palindromes[-1] = [[]]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:
                    for each in palindromes[j]:
                        palindromes[i].append([s[i:j]] + each)
        
        return palindromes[0]