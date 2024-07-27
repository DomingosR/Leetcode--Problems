class Solution(object):
    def fallingSquares(self, positions):
        heights, leftPos = [0], [0]
        maxHeight = 0
        tallest = []

        for left, side in positions:
            i = bisect_right(leftPos, left)
            j = bisect_left(leftPos, left + side)
            high = max(heights[i-1:j] or [0]) + side

            leftPos[i:j] = [left, left + side]
            heights[i:j] = [high, heights[j-1]]
            
            maxHeight = max(maxHeight, high)
            tallest.append(maxHeight)

        return tallest