class Solution(object):
    def concatenatedBinary(self, n):
        p = 10 ** 9 + 7
        currentNum, length, count = 1, 2, 2
        
        for num in range(2, n+1):
            currentNum = ((2 ** length) * currentNum + num) % p
            count -= 1
            if count == 0:
                length += 1
                count = 2 ** (length - 1)
        
        return currentNum