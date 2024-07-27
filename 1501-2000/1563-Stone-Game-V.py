import numpy as np

def solveGame_On2_Adapted(inputArray):
    #
    # This function uses the one above as a template, and makes the
    # following modification for efficiency:
    #
    # (1) For given i, the value of k described above for the subarray
    #     i..j increases gradually as j increases (or decreases as i
    #     decreases).  We take advantage of this fact to eliminate the
    #     binary search above, which saves even more time.

    numStones = len(inputArray)

    # *** Creating arrays to hold game information ***
    gameValueArray = np.zeros((numStones, numStones))
    leftOptimum = np.zeros((numStones, numStones))  # Only applies to i <= j
    rightOptimum = np.zeros((numStones, numStones)) # Only applies to i <= j

    for i in range(numStones):
        leftOptimum[i][i] = inputArray[i]
        rightOptimum[i][i] = inputArray[i]

    # *** Inner loop to fill gameValueArray ***
    for j in range(1, numStones):
        k = j
        currentSum = inputArray[j]
        rightSum = 0
        for i in range(j-1, -1, -1):
            currentSum += inputArray[i]
            while(2 * (rightSum + inputArray[k]) <= currentSum):
                rightSum += inputArray[k]
                k -= 1
            if (2 * rightSum == currentSum):
                gameValueArray[i][j] = leftOptimum[i][k]
            else:
                if (k == i):
                    gameValueArray[i][j] = 0
                else:
                    gameValueArray[i][j] = leftOptimum[i][k-1]
            if (k != j):
                gameValueArray[i][j] = max(gameValueArray[i][j], rightOptimum[k+1][j])

            leftOptimum[i][j] = max(leftOptimum[i][j-1], gameValueArray[i][j] + currentSum)
            rightOptimum[i][j] = max(rightOptimum[i+1][j], gameValueArray[i][j] + currentSum)

    return int(gameValueArray[0][numStones - 1])

class Solution(object):
    def stoneGameV(self, stoneValue):
        return(solveGame_On2_Adapted(stoneValue))