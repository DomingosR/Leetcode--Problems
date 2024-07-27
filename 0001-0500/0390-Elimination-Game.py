class Solution(object):
    def lastRemaining(self, n):
        first, last, count = 1, n, n
        step, diff = 1, 1
        
        while count > 1:
            if step % 2:
                first += diff
                last -= diff if count % 2 else 0
            else:
                last -= diff
                first += diff if count % 2 else 0
            
            count //= 2
            diff *= 2
            step += 1
            
        return first