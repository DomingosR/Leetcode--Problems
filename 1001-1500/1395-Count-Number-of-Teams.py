from sortedcontainers import SortedList

class Solution(object):
    def numTeams(self, rating):
        def countElementsOnSides(val, refList):
            lowerElements = refList.bisect_left(val)
            higherElements = len(refList) - refList.bisect_right(val)
            return lowerElements, higherElements
        
        numValidTeams = 0
        leftList = SortedList(rating[:1])
        rightList = SortedList(rating[1:])

        for val in rating[1:]:
            rightList.remove(val)
            lowerLeft, higherLeft = countElementsOnSides(val, leftList)
            lowerRight, higherRight = countElementsOnSides(val, rightList)
            numValidTeams += (lowerLeft * higherRight + higherLeft * lowerRight)
            leftList.add(val)
        
        return numValidTeams