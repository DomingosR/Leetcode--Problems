class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        startTimes = [start for start, end in flowers]
        endTimes = [end for start, end in flowers]
        startTimes.sort()
        endTimes.sort()
        
        numFlowers = []
        for person in people:
            numFlowers.append(bisect_right(startTimes, person) - bisect_left(endTimes, person))
        
        return numFlowers