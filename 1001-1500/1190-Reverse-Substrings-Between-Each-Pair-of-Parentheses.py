class Solution(object):
    def reverseParentheses(self, s):
        strStack = [""]
        
        for char in s:
            if char == "(":
                strStack.append("")
            elif char == ")":
                lastVal = strStack.pop()
                strStack[-1] += lastVal[::-1]
            else:
                strStack[-1] += char
        
        return strStack[0]