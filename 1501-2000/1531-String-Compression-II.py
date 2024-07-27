class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        # Auxiliary function to compute length of number converted to string
        def lenNum(inputNum):
            if inputNum == 1:
                return 1
            if inputNum < 10:
                return 2
            if inputNum < 100:
                return 3
            return 4

        # Preliminaries
        n = len(s)
        largeNum = 1000
        dp = [[largeNum] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0

        # In the loop, i denotes the length of the left substring considered, and
        # j denotes the number of characters deleted so far
        for i in range(n+1):
            for j in range(min(i, k) + 1):
                if j > 0:
                    dp[i][j] = dp[i-1][j-1]

                remove, count = 0, 0
                for l in range(i, 0, -1):
                    if s[l-1] == s[i-1]:
                        count += 1
                    else:
                        remove += 1
                        if remove > j:
                            break
                    dp[i][j] = min(dp[l-1][j-remove] + lenNum(count), dp[i][j])

        return dp[-1][-1]