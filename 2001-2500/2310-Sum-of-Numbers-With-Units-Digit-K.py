class Solution(object):
    def minimumNumbers(self, num, k):
        if num == 0:
            return 0
            
        lastDigit = num % 10
        for mult in range(1, 11):
            if mult * k % 10 == lastDigit and mult * k <= num:
                return mult
        return -1