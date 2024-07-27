def timeToRot(grid):
    m = len(grid)         # Number of rows
    n = len(grid[0])      # Number of columns

    # Create a grid which will ultimately contain the minimum distance to a rotten orange
    # Initially this will be zero for a rotten orange, -1 for a normal orange which cannot
    # be rotted, and -2 for an empty square.
    distanceToRotten = [[(grid[i][j] - 2) for j in range(n)] for i in range(m)]

    # Function that checks whether a given value is present on the distanceToRotten array
    def searchValue(inputVal):
        numValues = sum(sum(1 if distanceToRotten[i][j]== inputVal else 0 for j in range(n)) for i in range(m))
        if numValues > 0:
            return True
        return False

    # If there are no fresh oranges, return 0
    if not searchValue(-1):
        return 0

    # If there are fresh oranges, perform recursion to determine the furthest away a fresh orange is from
    # a rotten one
    changesMade = 1
    currentRound = 0

    while changesMade == 1:
        changesMade = 0
        for i in range(m):
            for j in range(n):
                if distanceToRotten[i][j] == currentRound:
                    if i > 0 and distanceToRotten[i-1][j] == -1:
                        distanceToRotten[i-1][j] = currentRound + 1
                        changesMade = 1
                    if j > 0 and distanceToRotten[i][j-1] == -1:
                        distanceToRotten[i][j-1] = currentRound + 1
                        changesMade = 1
                    if i < m-1 and distanceToRotten[i+1][j] == -1:
                        distanceToRotten[i+1][j] = currentRound + 1
                        changesMade = 1
                    if j < n-1 and distanceToRotten[i][j+1] == -1:
                        distanceToRotten[i][j+1] = currentRound + 1
                        changesMade = 1
        if changesMade == 1:
            currentRound += 1

    # If there are still fresh oranges left, they are unreachable
    if searchValue(-1):
        return -1
    else:
        return currentRound

class Solution(object):
    def orangesRotting(self, grid):
        return timeToRot(grid)
