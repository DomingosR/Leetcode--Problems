def surfaceAreaOf3DShapes(grid):
    n = len(grid)

    # First, compute area above and below shape
    totalSum = 0
    for i in range(n):
        totalSum += 2 * sum([1 if j > 0 else 0 for j in grid[i]])

    # Then, compute area on north and south faces of shape
    for i in range(n+1):
        if i == 0:
            for j in range(n):
                totalSum += abs(grid[i][j])
        elif i == n:
            for j in range(n):
                totalSum += abs(grid[i-1][j])
        else:
            for j in range(n):
                totalSum += abs(grid[i][j] - grid[i-1][j])

    # Then, compute area on east and west faces of shape
    for j in range(n+1):
        if j == 0:
            for i in range(n):
                totalSum += abs(grid[i][j])
        elif j == n:
            for i in range(n):
                totalSum += abs(grid[i][j-1])
        else:
            for i in range(n):
                totalSum += abs(grid[i][j] - grid[i][j-1])

    return totalSum

class Solution(object):
    def surfaceArea(self, grid):
        return surfaceAreaOf3DShapes(grid)
