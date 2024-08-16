class Solution(object):
    def numTeams(self, rating):
        leftCount = defaultdict(list)
        n = len(rating)
        order = []
        
        for i in range(n):
            indRating = rating[i]
            insertPos = bisect.bisect(order, indRating)
            order[insertPos:insertPos] = [indRating]
            leftCount[indRating] = [insertPos, i - insertPos]
        
        
        order = []
        numTeams = 0
        for i in range(n-1, -1, -1):
            indRating = rating[i]
            insertPos = bisect.bisect(order, indRating)
            order[insertPos:insertPos] = [indRating]
            numTeams += (leftCount[indRating][1] * insertPos + leftCount[indRating][0] * (n - 1 - i - insertPos))
  
        return numTeams