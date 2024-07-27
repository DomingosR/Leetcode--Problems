class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        previousValues = defaultdict(int)
        largeNum = 100001

        # dp(i, k) is the difficulty of jobDifficulty[i:]
        # when on day k jobs [i:] are left to do
        def dp(i, j):
            if (i, j) not in previousValues:
                if j == d:
                    previousValues[(i, j)] = max(jobDifficulty[i:])
                else:
                    returnVal = largeNum
                    currentDifficulty = 0
                    for k in range(i, n-d+j):
                        currentDifficulty = max(currentDifficulty, jobDifficulty[k])
                        returnVal = min(returnVal, currentDifficulty + dp(k+1, j+1))
                    previousValues[(i, j)] = returnVal

            return previousValues[(i, j)]

        return -1 if n < d else dp(0, 1)
