class Solution(object):
    def closestDivisors(self, num):
        maxVal = int(sqrt(num + 2))
        
        for i in range(maxVal, 0, -1):
            if (num + 1) % i == 0:
                return [(num + 1) // i, i]
            if (num + 2) % i == 0:
                return [(num + 2) // i, i]