class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if tomatoSlices % 2 or not (2 * cheeseSlices <= tomatoSlices <= 4 * cheeseSlices):
            return []
        
        nJumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        nSmall = cheeseSlices - nJumbo
        
        return [nJumbo, nSmall]