class Solution(object):
    def ways(self, pizza, k):
        p = 10**9 + 7

        n = len(pizza)
        m = len(pizza[0])

        # Extending pizza one row and column
        for i in range(n):
            pizza[i] += "."
        pizza.append("." * (m+1))

        # Computing number of apples left in cells below and to the right
        remaining = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                remaining[i][j] = remaining[i+1][j] + remaining[i][j+1] \
                                    - remaining[i+1][j+1] + (1 if pizza[i][j] == "A" else 0)

        # Entries in the dict are of the form (i, j, numPieces): n, where there are n ways to
        # cut pizza[i:][j:] into numPieces parts, each with at least one apple
        numWays = defaultdict()

        def dp(i, j, numPieces):
            # First, look up value in dictionary
            if (i, j, numPieces) in numWays:
                return numWays[(i, j, numPieces)]

            # Then, consider terminal cases (last row and last column)
            if numPieces == 1:
                returnVal = 1 if remaining[i][j] > 0 else 0
                numWays[(i, j, numPieces)] = returnVal
                return returnVal

            # We consider cuts below row i1 (i1 = i, i+1, ..., n-2) or to the right of column
            # j1 (j1 = j, j+1, ..., m-2)
            returnVal = 0

            for i1 in range(i, n-1):
                if numPieces - 1 <= remaining[i1 + 1][j] < remaining[i][j]:
                    returnVal += dp(i1 + 1, j, numPieces - 1)

            for j1 in range(j, m-1):
                if numPieces - 1 <= remaining[i][j1 + 1] < remaining[i][j]:
                    returnVal += dp(i, j1 + 1, numPieces - 1)

            numWays[(i, j, numPieces)] = returnVal % p
            return returnVal % p

        return dp(0, 0, k)
