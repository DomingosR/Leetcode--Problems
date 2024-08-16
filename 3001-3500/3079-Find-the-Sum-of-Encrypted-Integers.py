class Solution(object):
    def sumOfEncryptedInt(self, nums):
        def encrypt(n):
            largest, nLen = 0, 0
            while n > 0:
                largest = max(largest, n % 10)
                nLen += 1
                n //= 10
            return largest * int("1" * nLen)
        
        return sum([encrypt(num) for num in nums])