import numpy as np

def longestValid(inputStr):
    while inputStr[0:1] == ")":
        inputStr = inputStr[1:]

    print(inputStr)

    numChars = len(inputStr)
    cumSum = np.zeros(numChars + 1, dtype=np.intc)
    cumSum[0] = 0
    maxSum = int(0)
    minSum = int(0)

    for i in range(1, numChars + 1):
        if inputStr[i-1:i] == "(":
            cumSum[i] = cumSum[i-1] + 1
            maxSum = max(maxSum, cumSum[i])
        if inputStr[i-1:i] == ")":
            cumSum[i] = cumSum[i-1] - 1
            minSum = min(minSum, cumSum[i])

    # In the following array, position i corresponds to a cumulative sum
    # of (i - minSum)
    auxArray = -np.ones(maxSum - minSum + 1, dtype=np.intc)
    auxArray[-minSum] = 0
    maxLength = 0

    for i in range(1, numChars + 1):
        if inputStr[i-1:i] == "(":
            auxArray[cumSum[i] - minSum] = i
        else:
            if auxArray[cumSum[i-1] - minSum] >= 0:
                maxLength = max(maxLength, (i-1) - auxArray[cumSum[i-1] - minSum])
                auxArray[cumSum[i-1] - minSum] = -1

            if auxArray[cumSum[i] - minSum] >= 0:
                maxLength = max(maxLength, i - auxArray[cumSum[i] - minSum])
            else:
                auxArray[cumSum[i] - minSum] = i

    return maxLength

class Solution(object):
    def longestValidParentheses(self, s):
        return longestValid(s)