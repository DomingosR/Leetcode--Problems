class Solution(object):
    def makeGood(self, s):
        if len(s) < 2: return s
        
        def removeChars(inputStr):
            if len(inputStr) < 2:
                return inputStr
            
            for i in range(1, len(inputStr)):
                thisChar = inputStr[i-1]
                nextChar = inputStr[i]
                if thisChar != nextChar and thisChar.lower() == nextChar.lower():
                    reducedString = inputStr[:i-1] + inputStr[i+1:]
                    return removeChars(reducedString)
                
            return inputStr
        
        return removeChars(s)