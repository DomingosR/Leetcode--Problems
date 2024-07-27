def divideIntegers(dividend, divisor):
    if dividend == 0:
        return 0

    # First, find the signs of the numbers
    signDividend = +1 if dividend > 0 else -1
    signDivisor = +1 if divisor > 0 else -1

    # Perform division between the absolute values of the numbers
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Arrays for division
    multiplier = [1]
    multiplesOfDivisor = [divisor]

    auxNum1 = 2
    auxNum2 = divisor + divisor

    while auxNum2 + auxNum2 < dividend:
        multiplier.append(auxNum1)
        multiplesOfDivisor.append(auxNum2)
        auxNum1 += auxNum1
        auxNum2 += auxNum2

    numElements = len(multiplier)

    i = numElements - 1
    quotient = 0

    while i >= 0:
        currentElement = multiplesOfDivisor[i]
        currentMultiplier = multiplier[i]
        while currentElement <= dividend:
            quotient += currentMultiplier
            dividend -= currentElement
        i -= 1

    auxQuotient = quotient * signDividend * signDivisor

    if auxQuotient > 2147483647:
        return 2147483647
    elif auxQuotient < -2147483648:
        return -2147483648
    else:
        return auxQuotient

class Solution(object):
    def divide(self, dividend, divisor):
        return divideIntegers(dividend, divisor)
