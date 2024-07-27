class Solution(object):
    def winnerOfGame(self, colors):
        validACount, validBCount = 0, 0
        
        for i in range(1, len(colors) - 1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == "A":
                    validACount += 1
                else:
                    validBCount += 1
        
        return validACount > validBCount