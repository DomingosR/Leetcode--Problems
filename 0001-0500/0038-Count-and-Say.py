class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        prevVal = self.countAndSay(n-1)
        nextSeq = ""
            
        for i in range(len(prevVal)):
            if i == 0:
                currChar = prevVal[0]
                currCount = 1
            else:
                if prevVal[i] == currChar:
                    currCount += 1
                else:
                    nextSeq += str(currCount) + str(currChar)
                    currChar = prevVal[i]
                    currCount = 1
                    
        nextSeq += str(currCount) + str(currChar)
        return nextSeq