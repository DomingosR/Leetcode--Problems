class Solution(object):
    def missingRolls(self, rolls, mean, n):
        missingSum = (len(rolls) + n) * mean - sum(rolls)
        
        if missingSum < n or missingSum > 6 * n:
            return []
        
        k = missingSum - n * (missingSum // n)
        return [missingSum // n] * (n - k) + [missingSum // n + 1] * k