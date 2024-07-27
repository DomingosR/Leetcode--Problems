class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        numLetters = len(s)
        indices = [i for i in range(numLetters) if i % (2 * (numRows - 1)) == 0]

        leftNum = 1
        rightNum = 2 * numRows - 3

        while leftNum <= rightNum:
            modulo = {leftNum, rightNum}
            indices += [i for i in range(numLetters) if i % (2 * (numRows - 1)) in modulo]
            leftNum += 1
            rightNum -= 1

        return "".join([s[indices[i]] for i in range(numLetters)])
