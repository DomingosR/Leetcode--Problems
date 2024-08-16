class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        
        smallNums = ["One", "Two", "Three", "Four", "Five", "Six", \
                     "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", \
                     "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", \
                     "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        groups = ["Thousand", "Million", "Billion"]
        
        def processSubstr(inputStr, groupNo, groupCount):
            auxStr = ""
            
            if int(inputStr) == 0:
                return auxStr
            
            if groupNo > 0:
                auxStr += " "
            
            if int(inputStr[0]) > 0:
                auxStr += smallNums[int(inputStr[0]) - 1] + " Hundred"
                
            if inputStr[1:] != "00":
                if inputStr[0] != "0":
                    auxStr += " "
                if int(inputStr[1:]) < 20:
                    auxStr += smallNums[int(inputStr[1:]) - 1]
                elif int(inputStr[1]) > 0:
                    auxStr += tens[int(inputStr[1]) - 2]
                    if int(inputStr[2]) > 0:
                        auxStr += (" " + smallNums[int(inputStr[2]) - 1])
                else:
                    auxStr += (" " + smallNums[int(inputStr[2]) - 1])
                        
            if groupNo < groupCount - 1:
                auxStr += (" " + groups[groupCount - groupNo - 2])
                
            return auxStr
                
        numStr = str(num)
        strLen = len(numStr)
        numGroups = (strLen + 2) // 3
        
        if strLen % 3:
            numStr = "0" * (3 - (strLen % 3)) + numStr
        
        finalStr = ""
        
        for i in range(numGroups):
            finalStr += processSubstr(numStr[3 * i: 3 * i + 3], i, numGroups)
            
        return finalStr