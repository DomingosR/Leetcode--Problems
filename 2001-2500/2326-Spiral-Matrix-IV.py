class Solution(object):
    def spiralMatrix(self, m, n, head):
        finalMatrix = [[-1] * n for _ in range(m)]
        directions = [0, 1, 0, -1, 0]
        currentRow, currentCol, currentDir = 0, 0, 0
        dRow, dCol = directions[currentDir], directions[currentDir + 1]
        currentNode = head
        
        while currentNode:
            finalMatrix[currentRow][currentCol] = currentNode.val
            nextRow, nextCol = currentRow + dRow, currentCol + dCol
            if not ((m > nextRow >= 0 <= nextCol < n) and finalMatrix[nextRow][nextCol]) == -1:
                currentDir = (currentDir + 1) % 4
                dRow, dCol = directions[currentDir], directions[currentDir + 1]
                currentRow, currentCol = currentRow + dRow, currentCol + dCol
            else:
                currentRow, currentCol = nextRow, nextCol
            currentNode = currentNode.next
            
        return finalMatrix