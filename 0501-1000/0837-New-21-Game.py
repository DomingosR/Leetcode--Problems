class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts:
            return 1.0

        prob = [1.0] + [0] * n
        auxSum = 1.0
        
        for i in range(1, n+1):
            prob[i] = auxSum / maxPts
            if i < k:
                auxSum += prob[i]
            if i >= maxPts:
                auxSum -= prob[i-maxPts]
        
        return sum(prob[k:])