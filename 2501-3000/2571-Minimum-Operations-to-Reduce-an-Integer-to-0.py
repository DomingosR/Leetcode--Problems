class Solution(object):
    def minOperations(self, n):
        def processNum(num):
            if num == 0:
                return 0
            
            while num % 2 == 0:
                num //= 2
                
            if num & 2:
                return processNum(num + 1) + 1
            else:
                return processNum(num - 1) + 1
            
        return processNum(n)