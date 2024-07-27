class Solution(object):
    def decodeString(self, s):
        currentNum = 0
        numStack = []
        strStack = [""]

        for i, currentChar in enumerate(s):
            if currentChar.isdigit():
                currentNum = 10 * currentNum + int(currentChar)
            elif currentChar == "[":
                numStack.append(currentNum)
                currentNum = 0
                strStack.append("")
            elif currentChar == "]":
                currentStr = strStack.pop()
                prevStr = strStack.pop()
                repetitions = numStack.pop()
                strStack.append(prevStr + currentStr * repetitions)
            else:
                strStack[-1] += currentChar

        return strStack[0]
