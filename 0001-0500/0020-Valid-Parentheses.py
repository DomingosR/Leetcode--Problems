class Solution(object):
    def isValid(self, s):
        openBracket = []
        leftBrackets = ["(", "[", "{"]
        rightBrackets = [")", "]", "}"]

        for i in range(len(s)):
            nextChar = s[i]
            if nextChar in leftBrackets:
                openBracket.append(nextChar)
            else:
                if not openBracket:
                    return False
                auxChar = openBracket.pop()
                if leftBrackets[rightBrackets.index(nextChar)] != auxChar:
                    return False
        
        return False if openBracket else True