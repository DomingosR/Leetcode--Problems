def isSplitPossible(nums):
    prevElement = None
    prevSeq1 = 0
    prevSeq2 = 0
    prevSeq3 = 0

    i = 0
    while i < len(nums):
        currElement = nums[i]
        countElement = 0
        while i < len(nums) and nums[i] == currElement:
            countElement += 1
            i += 1

        if prevElement is None or currElement != prevElement + 1:
            if prevSeq1 or prevSeq2:
                return False

            currSeq1 = countElement
            currSeq2 = 0
            currSeq3 = 0

        else:
            if prevSeq1 + prevSeq2 > countElement:
                return False

            currSeq2 = prevSeq1
            currSeq3 = prevSeq2 + min(prevSeq3, countElement - (prevSeq1 + prevSeq2))
            currSeq1 = max(0, countElement - prevSeq1 - prevSeq2 - prevSeq3)

        prevElement = currElement
        prevSeq1 = currSeq1
        prevSeq2 = currSeq2
        prevSeq3 = currSeq3

    return not prevSeq1 and not prevSeq2

class Solution(object):
    def isPossible(self, nums):
        return isSplitPossible(nums)