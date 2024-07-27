class Solution(object):
    def numRollsToTarget(self, n, k, target):
        if target < n or target > n*k:
            return 0

        p = 10**9 + 7
        
        # Initial number of ways, if there is a single roll of the die
        currentWays = [0] + [1] * k + [0] * (target - k)

        # Loop to compute effect of (n-1) additional dies
        for i in range(n-1):
            nextWays = [0] * (target + 1)
            currentSum = currentWays[i+1]
            maxSum = min((i+2)*k, target)

            for j in range(i+2, maxSum + 1):
                nextWays[j] = currentSum
                currentSum += currentWays[j]
                if j >= k+i+1:
                    currentSum -= currentWays[j-k]

            currentWays = nextWays
        
        # Return value
        return currentWays[target] % p