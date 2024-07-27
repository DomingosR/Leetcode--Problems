class Solution(object):
    def maximumSwap(self, num):
        numStr = str(num)
        n = len(numStr)
        numDigits = [int(numStr[i]) for i in range(n)]
        swapIndex1, swapIndex2, maxIndex = 0, 0, n-1
        
        for i in range(n-1, -1, -1):
            if numDigits[i] > numDigits[maxIndex]:
                maxIndex = i
            elif numDigits[i] < numDigits[maxIndex]:
                swapIndex1, swapIndex2 = i, maxIndex
                
        numDigits[swapIndex1], numDigits[swapIndex2] = numDigits[swapIndex2], numDigits[swapIndex1]
        
        return int("".join([str(num) for num in numDigits]))