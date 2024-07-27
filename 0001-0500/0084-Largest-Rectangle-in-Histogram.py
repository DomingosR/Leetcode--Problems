class Solution(object):
    def largestRectangleArea(self, heights):
        maxArea = 0
        previous = []
        n = len(heights)
        
        for i, h in enumerate(heights):
            if not previous or h > previous[-1][1]:
                previous.append((i, h))
            else:
                while previous and previous[-1][1] >= h:
                    j, prevH = previous.pop()
                    maxArea = max(maxArea, (i - j) * prevH)
                previous.append((j, h))
            
        while previous:
            j, prevH = previous.pop()
            maxArea = max(maxArea, (n-j) * prevH)
            
        return maxArea