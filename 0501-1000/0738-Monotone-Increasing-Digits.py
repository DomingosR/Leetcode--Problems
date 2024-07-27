class Solution(object):
    def monotoneIncreasingDigits(self, n):
        def nextCandidate(n):
            numStr, i = str(n), 0
            while i < len(numStr) - 1:
                if int(numStr[i+1]) < int(numStr[i]):
                    break
                i += 1
                
            if i == len(numStr) - 1:
                return n
            
            nextNumStr = numStr[:i]
            nextNumStr += str(int(numStr[i]) - 1)
            nextNumStr += "9" * (len(numStr) - i - 1)
        
            return nextCandidate(int(nextNumStr))
        
        return nextCandidate(n)