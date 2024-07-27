class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        n = len(dist)
        
        if hour <= n-1:
            return -1
        
        def arrivalTime(speed):
            return sum([(dist[i] + speed - 1) // speed for i in range(n-1)]) + 1.0 * dist[-1] / speed
        
        minSpeed = 1
        maxSpeed = 10 ** 7 + 1
        
        while minSpeed < maxSpeed:
            midSpeed = (minSpeed + maxSpeed) // 2
            if arrivalTime(midSpeed) <= hour:
                maxSpeed = midSpeed
            else:
                minSpeed = midSpeed + 1
        
        return minSpeed