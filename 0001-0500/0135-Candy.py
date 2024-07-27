class Solution:
    def candy(self, ratings):
        n = len(ratings)
        numCandy = [1] * n
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                numCandy[i+1] = max(1 + numCandy[i], numCandy[i+1])
                
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                numCandy[i] = max(1 + numCandy[i+1], numCandy[i])
        
        return sum(numCandy)