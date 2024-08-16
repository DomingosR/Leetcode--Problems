class Solution(object):
    def alphabetBoardPath(self, target):
        currentRow, currentCol = 0, 0
        moves = [""]
        
        def processRow(currentRow, currentCol, nextRow, nextCol):
            if nextRow < currentRow:
                moves[0] += "U" * (currentRow - nextRow)
            elif nextRow > currentRow:
                moves[0] += "D" * (nextRow - currentRow)
                
        def processCol(currentRow, currentCol, nextRow, nextCol):
            if nextCol < currentCol:
                moves[0] += "L" * (currentCol - nextCol)
            elif nextCol > currentCol:
                moves[0] += "R" * (nextCol - currentCol)            
        
        for char in target:
            order = ord(char) - ord('a')
            nextRow, nextCol = (order // 5), order % 5
            
            if currentRow == 5:
                processRow(currentRow, currentCol, nextRow, nextCol)
                processCol(currentRow, currentCol, nextRow, nextCol)
            else:
                processCol(currentRow, currentCol, nextRow, nextCol)  
                processRow(currentRow, currentCol, nextRow, nextCol)
              
            moves[0] += "!"
            currentRow, currentCol = nextRow, nextCol
            
        return moves[0]