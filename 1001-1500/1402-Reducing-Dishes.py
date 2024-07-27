class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse = True)
        currentSum = 0
        currentSatisfaction = 0

        for i in range(len(satisfaction)):
            currentSum += satisfaction[i]
            if currentSum < 0:
                break
            currentSatisfaction += currentSum

        return currentSatisfaction
