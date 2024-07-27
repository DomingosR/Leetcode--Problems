from collections import deque

def fillRange(image, sr, sc, color):
    if image[sr][sc] == color:
        return image

    originalColor = image[sr][sc]
    numRows = len(image)
    numCols = len(image[0])

    def processCell():
        i, j = queue.pop()
        image[i][j] = color
        if i+1 < numRows and image[i+1][j] == originalColor:
            queue.appendleft([i+1, j])
        if i-1 >= 0 and image[i-1][j] == originalColor:
            queue.appendleft([i-1, j])
        if j+1 < numCols and image[i][j+1] == originalColor:
            queue.appendleft([i, j+1])
        if j-1 >= 0 and image[i][j-1] == originalColor:
            queue.appendleft([i, j-1])

    queue = deque()
    queue.appendleft([sr, sc])
    while queue:
        processCell()

    return image

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        return fillRange(image, sr, sc, color)
