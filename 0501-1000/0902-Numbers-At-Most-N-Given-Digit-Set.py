class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        def numDigits(num):
            return len(str(num))
        
        def leadingDigit(num):
            return int(str(num)[0])
        
        def secondDigit(num):
            return int(str(num)[1:2])
        
        def countNums(digits, n, digitsStrict):
            digitsNumeric = [int(digit) for digit in digits]
            digitCount = numDigits(n)

            if digitCount == 1:
                return len([digit for digit in digitsNumeric if digit <= int(n)])

            totalNums = 0
            
            if not digitsStrict:
                for k in range(1, digitCount):
                    totalNums += (len(digits) ** k)

            for digit in digitsNumeric:
                if digit < leadingDigit(n):
                    totalNums += (len(digits) ** (digitCount - 1))
                elif digit == leadingDigit(n) and secondDigit(n) > 0:
                    auxNum = int(str(n)[1:])
                    totalNums += countNums(digits, auxNum, True)

            return totalNums
        
        return countNums(digits, n, False)