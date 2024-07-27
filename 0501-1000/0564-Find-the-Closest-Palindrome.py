def digitCount(inputStr):
    return len(inputStr)

def reverseDigits(inputStr):
    return inputStr[::-1]

def palindrome(numDigits, startStr):
    auxStr = startStr
    if (numDigits % 2 == 1):
        auxStr = auxStr[:-1]

    return (startStr + auxStr[::-1])

def closePalindrome(inputStr):
    numDigits = digitCount(inputStr)
    digitsToKeep = int((numDigits + (numDigits % 2))/2)
    startStr = inputStr[0:digitsToKeep:]
    return palindrome(numDigits, startStr)

def lowerPalindrome(inputStr):
    if inputStr == '1':
        return '0'
    
    numDigits = digitCount(inputStr)
    digitsToKeep = int((numDigits + (numDigits % 2))/2)
    startStr = inputStr[0:digitsToKeep:]
    
    if startStr == '1' + '0' * (digitsToKeep - 1):
        return '9' * (numDigits - 1)
    else:
        return palindrome(numDigits, str(int(startStr) - 1))

def upperPalindrome(inputStr):
    numDigits = digitCount(inputStr)
    digitsToKeep = int((numDigits + (numDigits % 2))/2)
    startStr = inputStr[0:digitsToKeep:]
    
    if startStr == '9' * digitsToKeep:
        return '1' + '0' * (numDigits - 1) + '1'
    else:
        return palindrome(numDigits, str(int(startStr) + 1))
        
def nearestPalindromeStr(inputStr):
    closeStr = closePalindrome(inputStr)
    lowerStr = lowerPalindrome(inputStr)
    upperStr = upperPalindrome(inputStr)

    inputNum = int(inputStr)
    closeNum = int(closeStr)
    lowerNum = int(lowerStr)
    upperNum = int(upperStr)
    
    if inputNum < closeNum:
        upperStr = closeStr
        upperNum = closeNum

    if inputNum > closeNum:
        lowerStr = closeStr
        lowerNum = closeNum
    
    if abs(inputNum - lowerNum) <= abs(inputNum - upperNum):
        return lowerStr
    else:
        return upperStr
    
class Solution: 
    def nearestPalindromic(self, n):
        return nearestPalindromeStr(n)