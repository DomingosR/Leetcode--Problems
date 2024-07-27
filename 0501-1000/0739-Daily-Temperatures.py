class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        dateQueue = []
        returnVal = [0] * n

        for i in range(n):
            currentTemperature = temperatures[i]
            while dateQueue and temperatures[dateQueue[-1]] < currentTemperature:
                j = dateQueue.pop()
                returnVal[j] = i - j
            dateQueue.append(i)

        return returnVal