class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key = lambda x: x[0] - x[1])
        minEnergy, energyLeft = 0, 0
        
        for spent, minimum in tasks:
            minEnergy += max(minimum - energyLeft, 0)
            energyLeft += max(minimum - energyLeft, 0) - spent
            
        return minEnergy