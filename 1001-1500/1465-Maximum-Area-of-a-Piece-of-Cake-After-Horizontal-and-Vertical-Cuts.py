p = 1000000007

def maxAreaAfterCuts(h, w, horizontalCuts, verticalCuts):
    auxVert = [0] + sorted(horizontalCuts) + [h]
    auxHor = [0] + sorted(verticalCuts) + [w]

    maxHeight = 0
    for i in range(1, len(auxVert)):
        maxHeight = max(auxVert[i] - auxVert[i-1], maxHeight)
    
    maxWidth = 0
    for i in range(1, len(auxHor)):
        maxWidth = max(auxHor[i] - auxHor[i-1], maxWidth)    
    return (maxWidth * maxHeight % p)

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        return maxAreaAfterCuts(h, w, horizontalCuts, verticalCuts)