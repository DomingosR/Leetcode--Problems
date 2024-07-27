class Solution(object):
    def maximumOddBinaryNumber(self, s):
        n = len(s)
        onesCount = 0

        for indChar in s:
            onesCount += (1 if indChar == "1" else 0)

        zerosCount = n - onesCount

        return "1" * (onesCount - 1) + "0" * zerosCount + "1" 
