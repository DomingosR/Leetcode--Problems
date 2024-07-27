class Solution(object):
    def isNumber(self, s):
        allDigits = set("0123456789")
        
        def isAllDigits(s):
            stringChars = set(s)
            return stringChars.issubset(allDigits)
        
        def isValidDecimal(s):
            if len(s) == 0 or s.count(".") > 1:
                return False

            if s[0] == "+" or s[0] == "-":
                s = s[1:]
            
            stringChars = set(s)
            stringCharsAux = stringChars.difference({"."})
            return len(stringCharsAux) > 0 and stringCharsAux.issubset(allDigits)
        
        def isValidInteger(s):
            if len(s) == 0:
                return False
            
            if s[0] == "+" or s[0] == "-":
                s = s[1:]
            
            stringChars = set(s)
            return len(stringChars) > 0 and stringChars.issubset(allDigits)

        def isValidNumber(s):
            if s.count("e") + s.count("E") == 1:
                if s.count("e") == 1:
                    ePos = s.index("e")
                else:
                    ePos = s.index("E")
                sPart1 = s[:ePos]
                sPart2 = s[(ePos + 1):]
                
                return isValidDecimal(sPart1) and isValidInteger(sPart2)
            
            else:
                return isValidDecimal(s)
        
        return isValidNumber(s)