def isReorderedPowerOfTwo(inputNum):
    powersOfTwo = [1] * 30
    numDigits = [1] * 30

    for i in range(29):
        powersOfTwo[i+1] = 2 * powersOfTwo[i]
        numDigits[i+1] = len(str(powersOfTwo[i+1]))

    inputNumDigits = len(str(inputNum))
    inputDigitCounter = Counter(str(inputNum))
    testNums = [powersOfTwo[i] for i in range(30) if numDigits[i] == inputNumDigits]

    for num in testNums:
        if Counter(str(num)) == inputDigitCounter:
            return True

    return False

class Solution(object):
    def reorderedPowerOf2(self, n):
        return isReorderedPowerOfTwo(n)