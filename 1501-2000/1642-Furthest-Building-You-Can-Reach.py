class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        jumpHeights = []
        
        for i in range(len(heights)-1):
            if heights[i+1] - heights[i] > 0:
                heappush(jumpHeights, heights[i+1] - heights[i])
                if len(jumpHeights) > ladders:
                    bricks -= heappop(jumpHeights)
                    if bricks < 0:
                        return i
                    
        return len(heights) - 1