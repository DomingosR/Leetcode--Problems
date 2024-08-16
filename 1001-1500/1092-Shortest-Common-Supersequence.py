class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        m, n = len(str1), len(str2)
        partial = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    partial[i+1][j+1] = partial[i][j] + 1
                else:
                    partial[i+1][j+1] = max(partial[i+1][j], partial[i][j+1])
        
        auxStr, i, j = "", m-1, n-1
        while i >= 0 and j >= 0:
            if str1[i] == str2[j]:
                auxStr += str1[i]
                i -= 1
                j -= 1
            elif partial[i+1][j] < partial[i][j+1]:
                auxStr += str1[i]
                i -= 1
            else:
                auxStr += str2[j]
                j -= 1
        
        return str1[:i+1] + str2[:j+1] + auxStr[::-1]