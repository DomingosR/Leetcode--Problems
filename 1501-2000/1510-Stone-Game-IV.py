import numpy as np
import math

def solveGame(n):
    isWinningPosition = np.zeros(n+1)
    isWinningPosition[0] = 0

    for i in range(1, n+1):
        maxInt = int(math.sqrt(i))
        isWinningPosition[i] = not all(isWinningPosition[i - j**2] for j in range(1, maxInt + 1))

    return int(isWinningPosition[n])

class Solution(object):
    def winnerSquareGame(self, n):
        return(solveGame(n))