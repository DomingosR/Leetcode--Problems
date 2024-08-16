class Solution(object):
    def canBeValid(self, s, locked):
        n = len(s)
        if n % 2:
            return False
        
        # Do tests forward
        netOpen, wildCards = 0, 0
        for i in range(n):
            if locked[i] == "1":
                netOpen += (1 if s[i] == "(" else -1)
                if netOpen < 0:
                    if wildCards == 0:
                        return False
                    else:
                        netOpen += 1
                        wildCards -= 1
            else:
                wildCards += 1
            
        if netOpen > wildCards:
            return False
        
        # Do them backward
        netClosed, wildCards = 0, 0
        for i in range(n-1, -1, -1):
            if locked[i] == "1":
                netClosed += (1 if s[i] == ")" else -1)
                if netClosed < 0:
                    if wildCards == 0:
                        return False
                    else:
                        netClosed += 1
                        wildCards -= 1
            else:
                wildCards += 1
            
        if netClosed > wildCards:
            return False   
        
        return True