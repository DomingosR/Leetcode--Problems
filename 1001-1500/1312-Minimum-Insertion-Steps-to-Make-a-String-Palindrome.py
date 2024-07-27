class Solution(object):
    def minInsertions(self, s):
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[n - j - 1] \
                                   else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]
