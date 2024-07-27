class Solution(object):
    def findSubsequences(self, nums):
        def allSubseq(inputNums):
            if len(inputNums) == 1:
                return [[inputNums[0]]]

            prevSubseq = allSubseq(inputNums[:-1])
            lastNum = inputNums[-1]
            returnVal = [[lastNum]]

            for seq in prevSubseq:
                if seq not in returnVal:
                    returnVal += [seq]
                if lastNum >= seq[-1] and seq + [lastNum] not in returnVal:
                    returnVal += [seq + [lastNum]]

            return returnVal

        tempSeq = allSubseq(nums)
        return [seq for seq in tempSeq if len(seq) > 1]
