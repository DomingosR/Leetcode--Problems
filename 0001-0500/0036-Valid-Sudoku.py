class Solution(object):
    def isValidSudoku(self, inputBoard):
        def isValid(inputArray):
            auxVar = ''.join(inputArray).replace(".","")
            return len(auxVar) == len(set(auxVar))

        def checkRows():
            for row in inputBoard:
                if not isValid(row):
                    return False
            return True

        def checkCols():
            for col in zip(*inputBoard):
                if not isValid(col):
                    return False
            return True

        def checkSubsquares():
            for i in range(3):
                for j in range(3):
                    subBoard = [inputBoard[3*i + i1][3*j + j1] for i1 in range(3) for j1 in range(3)]
                    if not isValid(subBoard):
                        return False
            return True

        return (checkRows() and checkCols() and checkSubsquares())  
