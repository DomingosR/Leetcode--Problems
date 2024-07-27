from collections import defaultdict

def numCombinations(nums, target):
    numCombinationsDict = {0: 1}

    def getCount(k):
        if numCombinationsDict.get(k) != None:
            return numCombinationsDict.get(k)
        numsAux = [i for i in nums if i <= k]
        if not numsAux:
            return 0

        returnVal = 0
        for i in numsAux:
            returnVal += getCount(k-i)
        numCombinationsDict[k] = returnVal
        return returnVal

    return getCount(target)

class Solution(object):
    def combinationSum4(self, nums, target):
        return numCombinations(nums, target)
