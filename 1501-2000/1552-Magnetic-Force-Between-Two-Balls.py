class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        
        def numBalls(d):
            ballCount, currPos = 1, position[0]
            
            for i in range(1, len(position)):
                if position[i] - currPos >= d:
                    ballCount += 1
                    currPos = position[i]
            
            return ballCount
        
        lowDist, highDist = 0, position[-1] - position[0]
        
        while lowDist < highDist:
            midDist = highDist - (highDist - lowDist) // 2
            currNumBalls = numBalls(midDist)
            
            if currNumBalls >= m:
                lowDist = midDist
            else:
                highDist = midDist - 1
                
        return lowDist