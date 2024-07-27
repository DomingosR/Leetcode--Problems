def elementInMatrix(matrix, element):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    
    currentRow, currentCol = len(matrix) - 1, 0
    while currentRow >= 0 and currentCol <= len(matrix[0]) - 1:
        currentElement = matrix[currentRow][currentCol]
        if currentElement == element:
            return True
        if currentElement < element:
            currentCol += 1
        if currentElement > element:
            currentRow -= 1
    
    return False
        
class Solution(object):
    def searchMatrix(self, matrix, target):
        return elementInMatrix(matrix, target)