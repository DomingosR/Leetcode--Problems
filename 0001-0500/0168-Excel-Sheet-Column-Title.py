class Solution(object):
    def convertToTitle(self, columnNumber):
        colTitle = ""
        
        while columnNumber > 0:
            auxNum = (columnNumber - 1) % 26
            colTitle = chr(auxNum + 65) + colTitle
            columnNumber = (columnNumber - 1) // 26
        
        return colTitle
