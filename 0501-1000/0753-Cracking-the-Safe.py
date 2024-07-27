def shortestString(k, n):
    currentStr = "0" * (n - 1)
    visitedStrings = set()
    finalStr = currentStr
    iterationFinished = False

    while not iterationFinished:
        i = k - 1
        while i >= 0:
            trialStr = currentStr + str(i)
            if not trialStr in visitedStrings:
                finalStr += str(i)
                visitedStrings.add(trialStr)
                currentStr = trialStr[1:]
                break
            else:
                i -= 1
        if i < 0:
            iterationFinished = True

    return finalStr

class Solution(object):
    def crackSafe(self, n, k):
        return shortestString(k, n)