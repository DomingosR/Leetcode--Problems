class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for _ in range(m)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIndex = 0
        spiral = []
        i, j = 0, 0

        while m > i >= 0 <= j < n and visited[i][j] == 0:
            spiral.append(matrix[i][j])
            visited[i][j] = 1
            auxI, auxJ =  i + directions[dirIndex][0], j + directions[dirIndex][1]
            if m > auxI >= 0 <= auxJ < n and visited[auxI][auxJ] == 0:
                i, j = auxI, auxJ
            else:
                dirIndex = (dirIndex + 1) % 4
                i, j =  i + directions[dirIndex][0], j + directions[dirIndex][1]

        return spiral
