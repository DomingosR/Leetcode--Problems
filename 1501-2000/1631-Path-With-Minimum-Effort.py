class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        maxDist = m * n * 10**6 + 1
        
        distances = [[maxDist] * n for _ in range(m)]
        distances[0][0] = 0

        cellHeap = [(0, 0, 0)]  # Max effort to reach cell, row, column
        directions = [0, 1, 0, -1, 0]
        
        while cellHeap:
            dist, row, col = heappop(cellHeap)
            if dist > distances[row][col]:
                continue

            if row == m - 1 and col == n - 1:
                return dist
            
            distances[row][col] = dist
            
            for i in range(4):
                nextRow, nextCol = row + directions[i], col + directions[i+1]
                if m > nextRow >= 0 <= nextCol < n:
                    nextDist = max(dist, abs(heights[row][col] - heights[nextRow][nextCol]))
                    if nextDist < distances[nextRow][nextCol]:
                        distances[nextRow][nextCol] = nextDist
                        heappush(cellHeap, (nextDist, nextRow, nextCol))