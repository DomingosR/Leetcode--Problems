class Solution(object):
    def getMaximumGenerated(self, n):
        if n < 2:
            return n
        
        generated = [0] * (n+1)
        generated[1] = 1
        maxNum = 1
        
        for i in range(2, n+1):
            generated[i] = generated[i // 2] + generated[i // 2 + 1] * (i % 2)
            maxNum = max(maxNum, generated[i])
            
        return maxNum