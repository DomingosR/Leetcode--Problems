class Solution(object):
    def superpalindromesInRange(self, left, right):
        minVal = int(sqrt(int(left)))
        maxVal = int(sqrt(int(right)))
        
        def isPalindrome(num):
            numStr = str(num)
            return numStr == numStr[::-1]
        
        def nextPalindrome(num):
            if num < 9:
                return num + 1

            if num < 11:
                return 11

            numStr = str(num)
            k = len(numStr)
            leftStr, rightStr = numStr[:k//2], numStr[-(k//2):]
            leftVal, rightVal = int(leftStr), int(rightStr)

            if rightVal < int(leftStr[::-1]):
                return int(numStr[:-(k//2)] + leftStr[::-1])

            if k % 2:
                midVal = int(numStr[k//2])
                if midVal < 9:
                    return int(leftStr + str(midVal + 1) + leftStr[::-1])
                else:
                    nextLeftVal = leftVal + 1
                    if nextLeftVal < 10 ** (k//2):
                        return int(str(nextLeftVal) + "0" + str(nextLeftVal)[::-1])
                    else:
                        return 10 ** k + 1
            else:
                nextLeftVal = leftVal + 1
                if nextLeftVal < 10 ** (k//2):
                    return int(str(nextLeftVal) + str(nextLeftVal)[::-1])
                else:
                    return 10 ** k + 1 
        
        
        currentNum = nextPalindrome(minVal - 1)
        numSuperPals = 0
        while currentNum <= maxVal:
            numSuperPals += isPalindrome(currentNum ** 2)
            currentNum = nextPalindrome(currentNum)

        return numSuperPals