class Solution(object):
    def maxDepth(self, s):
        maxDepth = 0
        currDepth = 0

        for char in s:
            if char == "(":
                currDepth += 1
                maxDepth = max(maxDepth, currDepth)
            if char == ")":
                currDepth -= 1
        
        return maxDepth