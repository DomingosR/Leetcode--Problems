class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        
        smoothed = [[0] * n for _ in range(m)]
        directions = [(i, j) for i in range(-1, 2, 1) for j in range(-1, 2, 1)]
        
        for i in range(m):
            for j in range(n):
                adjacent = [(i + di, j + dj) for di, dj in directions if m > i+di >= 0 <= j + dj < n]
                smoothed[i][j] = sum([img[i1][j1] for i1, j1 in adjacent]) // len(adjacent)
                    
        return smoothed