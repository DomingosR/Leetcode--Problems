class Solution(object):
    def sequentialDigits(self, low, high):
        minLen = len(str(low))
        maxLen = min(len(str(high)), 9)
        auxStr = "123456789"
        allOnes = "1111111111"
        
        allNums = []
        
        for i in range(minLen, maxLen + 1):
            currentVal = int(auxStr[:i])
            increment = int(allOnes[:i])
            
            while currentVal < 10 ** i and currentVal % 10 > 0:
                if low <= currentVal <= high:
                    allNums.append(currentVal)
                currentVal += increment
        
        return allNums
            