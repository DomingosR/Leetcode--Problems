class Solution(object):
    def edgeScore(self, edges):
        n = len(edges)
        edgeScore = [0] * n
        maxScore = 0
        maxIndex = -1

        for i in range(n):
            targetIndex = edges[i]
            edgeScore[targetIndex] += i
            if edgeScore[targetIndex] > maxScore or \
                (edgeScore[targetIndex] == maxScore and targetIndex < maxIndex):
                maxScore = edgeScore[targetIndex]
                maxIndex = targetIndex
        
        return maxIndex