class Solution(object):
    def checkPartitioning(self, s):
        n = len(s)
        
        isPalindrome = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i >= j:
                    isPalindrome[i][j] = True
                elif s[i] == s[j]:
                    isPalindrome[i][j] = isPalindrome[i+1][j-1]

        for i in range(1, n):
            for j in range(i+1, n):
                if isPalindrome[0][i-1] and isPalindrome[i][j-1] and isPalindrome[j][n-1]:
                    return True
        return False
