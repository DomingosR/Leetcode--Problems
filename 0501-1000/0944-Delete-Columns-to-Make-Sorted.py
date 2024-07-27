class Solution(object):
    def minDeletionSize(self, strs):
        numStrs = len(strs)
        strLen = len(strs[0])

        orderedChars = list(map(list, zip(*strs)))
        minCharDiff = [min([ord(orderedChars[j][i]) - ord(orderedChars[j][i-1]) for i in range(1, numStrs)]) for j in range(strLen)]

        return len([i for i in range(strLen) if minCharDiff[i] < 0])
