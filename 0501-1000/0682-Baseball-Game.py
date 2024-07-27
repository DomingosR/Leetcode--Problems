class Solution(object):
    def calPoints(self, operations):
        scoreStack = []
        
        for token in operations:
            if token == "C":
                scoreStack.pop()
            elif token == "D":
                scoreStack.append(2 * scoreStack[-1])
            elif token == "+":
                scoreStack.append(scoreStack[-1] + scoreStack[-2])
            else:
                scoreStack.append(int(token))
                
        return sum(scoreStack)