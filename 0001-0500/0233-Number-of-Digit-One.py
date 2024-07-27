def countOfOnesV2(inputNum):
    if inputNum < 10:
        return (0 if inputNum == 0 else 1)
    else:
        return (1 if inputNum % 10 >= 1 else 0) + str(inputNum // 10).count('1') * (inputNum % 10 + 1) \
            + (inputNum // 10) + 10 * countOfOnesV2(inputNum // 10 - 1)

class Solution(object):
    def countDigitOne(self, n):
        return countOfOnesV2(n)