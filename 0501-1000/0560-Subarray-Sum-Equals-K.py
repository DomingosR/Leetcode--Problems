def computeNumSubarrays(inputArray, target):
    m = len(inputArray)
    partialSums = [0] * m

    for i in range(m):
        partialSums[i] = inputArray[i] + (partialSums[i-1] if i > 0 else 0)

    subArrayCount = 0
    auxSums = {0: 1}

    for i in range(m):
        subArrayCount += auxSums.get(partialSums[i] - target, 0)
        auxSums[partialSums[i]] = auxSums.get(partialSums[i], 0) + 1

    return subArrayCount

class Solution(object):
    def subarraySum(self, nums, k):
        return computeNumSubarrays(nums, k)
