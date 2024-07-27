class Solution(object):
    def countCollisions(self, directions):
        i, j = 0, len(directions) - 1
        
        while i <= j and directions[i] == "L":
            i += 1
            
        while i <= j and directions[j] == "R":
            j -= 1
        
        if i > j:
            return 0
        
        return sum([1 for k in range(i, j+1) if directions[k] != "S"])