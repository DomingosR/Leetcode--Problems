class Solution(object):
    def minimumDistance(self, word):
        def distVal(index1, index2):
            if index1 == 0:
			    return index1
            return abs(index1 // 6 - index2 // 6) + abs(index1 % 6 - index2 % 6)

        wordLen = len(word)
        maxVal = wordLen * 30

        currentDistances = {(0, 0): 0}
        nextDistances = {}
        wordCodes = [ord(char) + 1 for char in word]

        for code in wordCodes:
            for index1, index2 in currentDistances:
                nextDistances[code, index2] = min(nextDistances.get((code, index2), maxVal), currentDistances[index1, index2] + distVal(index1, code))
                nextDistances[index1, code] = min(nextDistances.get((index1, code), maxVal), currentDistances[index1, index2] + distVal(index2, code))
            currentDistances = nextDistances
            nextDistances = {}

        return min(currentDistances.values())
