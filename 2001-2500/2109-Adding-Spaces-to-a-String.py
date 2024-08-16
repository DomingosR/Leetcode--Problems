class Solution(object):
    def addSpaces(self, s, spaces):
        finalStr = []
        j = 0
        
        for i, char in enumerate(s):
            if j < len(spaces) and spaces[j] == i:
                finalStr.append(" ")
                j += 1
            finalStr.append(char)
            
        return "".join(finalStr)