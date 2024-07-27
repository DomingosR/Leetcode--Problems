class Solution(object):
    def makesquare(self, matchsticks):
        totalLength = sum(matchsticks)
        if totalLength % 4 != 0:
            return False

        numSticks = len(matchsticks)
        targetSide = totalLength // 4
        matchsticks.sort(reverse = True)
        currentSides = [0, 0, 0, 0]

        def processStick(i):
            if i == numSticks:
                return targetSide == currentSides[0] == currentSides[1] == currentSides[2]

            currentLen = matchsticks[i]
            for j in range(4):
                isZero = (currentSides[j] == 0)
                if currentSides[j] + currentLen <= targetSide:
                    currentSides[j] += currentLen
                    if processStick(i+1):
                        return True
                    currentSides[j] -= currentLen
                if isZero: break

            return False

        return processStick(0)
