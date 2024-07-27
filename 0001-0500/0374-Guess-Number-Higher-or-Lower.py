# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        lowerEnd = 1
        upperEnd = n
        
        while lowerEnd < upperEnd:
            midVal = (lowerEnd + upperEnd) // 2
            guessOutcome = guess(midVal)
            if guessOutcome == 0:
                return midVal
            elif guessOutcome == 1:
                lowerEnd = midVal + 1
            elif guessOutcome == -1:
                upperEnd = midVal - 1
        
        return lowerEnd