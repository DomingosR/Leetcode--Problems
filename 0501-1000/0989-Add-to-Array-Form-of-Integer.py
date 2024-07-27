class Solution(object):
    def addToArrayForm(self, num, k):
        intNum = 0
        for i in range(len(num)):
            intNum = 10 * intNum + num[i]
        resultStr = str(intNum + k)
        return [int(indChar) for indChar in resultStr]
