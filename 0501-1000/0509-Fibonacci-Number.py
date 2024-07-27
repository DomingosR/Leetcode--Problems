class Solution(object):
    def fib(self, n):
        if n < 2: return n
        
        f1, f2 = 0, 1
        
        for _ in range(n-1):
            f1, f2 = f2, f1 + f2
        
        return f2