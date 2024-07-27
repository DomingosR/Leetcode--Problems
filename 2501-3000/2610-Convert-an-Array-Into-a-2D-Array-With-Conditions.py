class Solution(object):
    def findMatrix(self, nums):
        numCounter = Counter(nums)
        finalMat = []

        while numCounter:
            nextRow = [i for i in numCounter.keys()]
            finalMat.append(nextRow)
            auxDict = {}
            for i in numCounter:
                if numCounter[i] > 1:
                    auxDict[i] = numCounter[i] - 1
            numCounter = auxDict

        return finalMat
