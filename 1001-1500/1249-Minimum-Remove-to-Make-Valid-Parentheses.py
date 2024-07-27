class Solution(object):
    def minRemoveToMakeValid(self, s):
        sList = list(s)
        indexStack = []

        for i, char in enumerate(sList):
            if char == "(":
                indexStack.append(i)
            if char == ")":
                if indexStack:
                    indexStack.pop()
                else:
                    sList[i] = ""
        
        while indexStack:
            sList[indexStack.pop()] = ""

        return "".join(sList)