class Solution(object):
    def minFlipsMonoIncr(self, s):
        n = len(s)
        sInt = [int(s[i]) for i in range(n)]
        leftSum = 0
        rightSum = sum(sInt)

        minVal = n - rightSum

        for i in range(n):
            leftSum += sInt[i]
            rightSum -= sInt[i]
            minVal = min(minVal, leftSum + n - (i+1) - rightSum)

        return minVal
