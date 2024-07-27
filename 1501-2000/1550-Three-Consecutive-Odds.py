class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        
        streak, i = 0, 0
        
        while i < len(arr):
            if arr[i] % 2:
                streak += 1
                if streak == 3:
                    return True
            else:
                streak = 0
            i += 1
            
        return False