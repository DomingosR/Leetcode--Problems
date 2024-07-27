class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        numBeds = len(flowerbed)
        numLeft = n
        
        if n == 0:
            return True

        if numBeds == 1:
            if n == 0 or (n == 1 and flowerbed[0] == 0):
                return True
            return False

        for i in range(numBeds):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                numLeft -= 1
            
            if i == numBeds-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                numLeft -= 1
            
            if 0 < i < numBeds-1 and flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                numLeft -= 1

            if numLeft == 0:
                return True

        return False 