	class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        
        sign = 1
        if num < 0:
            sign = -1
            num *= -1
        
        strRep = ""
        while num > 0:
            strRep = str(num % 7) + strRep
            num //= 7
        
        return strRep if sign == 1 else "-" + strRep