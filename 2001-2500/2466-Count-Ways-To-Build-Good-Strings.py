class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        dp = Counter({0: 1})
        p = 10**9 + 7
        
        for i in range(1, high+1):
            dp[i] = (dp[i-zero] + dp[i-one]) % p
                
        return sum([dp[i] for i in range(low, high + 1)]) % p