class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0":
            return 0

        n = len(s)

        def isValid(indStr):
            return 1 if (1 <= len(indStr) <= 2 \
                         and indStr[0] != "0" \
                         and int(indStr) <= 26) else 0

        numWays = [0] * (n+1)
        numWays[-1] = 1
        numWays[-2] = isValid(s[-1:])

        for i in range(n-2, -1, -1):
            numWays[i] = isValid(s[i:i+1]) * numWays[i+1] + \
                         isValid(s[i:i+2]) * numWays[i+2]

        return numWays[0]
