class Solution(object):
    def maxRunTime(self, n, batteries):
        batteries.sort()
        totalBattery = sum(batteries)
        
        while batteries[-1] > totalBattery // n:
            totalBattery -= batteries.pop()
            n -= 1
        
        return totalBattery // n
