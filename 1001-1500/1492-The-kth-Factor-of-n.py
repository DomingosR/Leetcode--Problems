class Solution(object):
    def kthFactor(self, n, k):
        count, currentNum = 0, 0
        factors1, factors2 = [], []
        
        while (currentNum + 1) ** 2 <= n:
            currentNum += 1
            if n % currentNum == 0:
                count += 1
                if count == k:
                    return currentNum
                
                factors1.append(currentNum)
                if currentNum ** 2 < n:
                    factors2.append(n // currentNum)
                    
        factors = factors1 + factors2[::-1]
        
        return -1 if len(factors) < k else factors[k-1]