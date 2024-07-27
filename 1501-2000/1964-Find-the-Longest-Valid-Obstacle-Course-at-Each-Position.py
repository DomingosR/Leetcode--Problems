class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        numCount = len(obstacles)
        tailElement = [0] * numCount

        currentSize = 0
        returnVal = []
        
        for num in obstacles:
            i = 0
            j = currentSize
            while i != j:
                m = (i + j)/2
                if obstacles[m] <= num:
                    i = m + 1
                else:
                    j = m
            obstacles[i] = num
            currentSize = max(currentSize, i+1)
            returnVal.append(i+1)

        return returnVal
