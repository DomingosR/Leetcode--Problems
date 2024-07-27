class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        minTimeToBloom = 0
        print(sorted(zip(growTime, plantTime)))
        for grow, plant in sorted(zip(growTime, plantTime)):
            minTimeToBloom = max(minTimeToBloom, grow) + plant
        return minTimeToBloom