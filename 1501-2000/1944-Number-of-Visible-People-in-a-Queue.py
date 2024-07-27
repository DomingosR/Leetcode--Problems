class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        numPeople = [0] * n
        stack = []
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                numPeople[stack.pop()] += 1
            if stack:
                numPeople[stack[-1]] += 1
            stack.append(i)
        
        return numPeople