class Solution(object):
    def minMaxDifference(self, num):
        numStr = str(num)
        for i in range(len(numStr)):
            if numStr[i] != "9":
                break
                
        maxNum = int(numStr.replace(numStr[i], "9"))
        minNum = int(numStr.replace(numStr[0], "0"))
        
        return maxNum - minNum