class Solution(object):
    def generateParenthesis(self, n):
        allCombinations = []
        
        def processState(openPar, closedPar, currentStr):
            if openPar + closedPar == 2 * n:
                allCombinations.append(currentStr)
                return
            
            if openPar < n:
                processState(openPar + 1, closedPar, currentStr + "(")
                
            if closedPar < openPar:
                processState(openPar, closedPar + 1, currentStr + ")")
                
        processState(0, 0, "")
        return allCombinations