class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        n = len(answerKey)
        falsePos = [i for i in range(n) if answerKey[i] == "F"]
        truePos = [i for i in range(n) if answerKey[i] == "T"]
        
        if max(len(falsePos), len(truePos)) >= n-k:
            return n
        
        falsePos = [-1] + falsePos + [n]
        truePos = [-1] + truePos + [n]
        
        maxDiff1 = max([falsePos[i+k+1] - falsePos[i] for i in range(len(falsePos) - k - 1)])
        maxDiff2 = max([truePos[i+k+1] - truePos[i] for i in range(len(truePos) - k - 1)])
        
        return max(maxDiff1, maxDiff2) - 1