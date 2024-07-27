class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * n
        maxVal = [0] * (n + 1)

        for i in range(n)[::-1]:
            points, skip = questions[i]
            dp[i] = points 
            if i + skip + 1 < n:
                dp[i] += maxVal[i + skip + 1]
            maxVal[i] = max(maxVal[i + 1], dp[i])
        
        return maxVal[0]