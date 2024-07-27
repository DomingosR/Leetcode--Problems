class Solution(object):
    def minimumOneBitOperations(self, n):
        def mostSignificantBit(num):
            # Example: returns 3 if 4 <= num < 7
            largestPower = 0
            while num > 0:
                largestPower += 1
                num >>= 1
            return largestPower
        
        def minimumOperations(num):
            if num <= 1:
                return num

            largestPower =  2 ** (mostSignificantBit(num) - 1)
            remainder = num - largestPower
            return  2 * largestPower - 1 - minimumOperations(remainder)
        
        return minimumOperations(n)