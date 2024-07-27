class Solution(object):
    def hasAlternatingBits(self, n):
        if n == 1:
            return True
        
        mask1, mask2 = 1, 2
        
        while mask1 <= n:
            if (mask1 & n) << 1 == (mask2 & n):
                return False
            mask1, mask2 = mask2, mask2 << 1
        
        return True