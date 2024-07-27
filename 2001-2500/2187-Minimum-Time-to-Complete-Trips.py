class Solution(object):
    def minimumTime(self, time, totalTrips):
        timeCounter = Counter(time)

        def numTrips(slottedTime):
            return sum([timeCounter[t] * (slottedTime // t) for t  in timeCounter.keys()])
        
        lowerVal = 1
        higherVal = totalTrips * max(timeCounter.keys())

        while lowerVal < higherVal:
            midVal = (lowerVal + higherVal) // 2

            if numTrips(midVal) >= totalTrips:
                higherVal = midVal
            else:
                lowerVal = midVal + 1
        
        return lowerVal