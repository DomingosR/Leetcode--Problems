class Solution(object):
    def rearrangeArray(self, nums):
        posNums = [n for n in nums if n > 0]
        negNums = [n for n in nums if n < 0]

        reordered = []

        for i in range(len(posNums)):
            reordered += [posNums[i], negNums[i]]

        return reordered