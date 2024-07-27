def checkForInterleaveV2(s1, s2, s3):
    # First, deal with trivial cases
    if len(s1) + len(s2) != len(s3):
        return False

    if len(s1) == 0:
        return True if s2 == s3 else False

    if len(s2) == 0:
        return True if s1 == s3 else False

    # Define a function to determine whether it's possible to interleave two strings starting
    # from positions (-i) and (-j), respectively, to produce the last (i+j) characters of
    # the given target string, and work recursively
    len1 = len(s1)
    len2 = len(s2)

    # This array contains (-1) if computation hasn't been done, 0 if the result is False, and 1 if it's True
    possibleArray = [[-1 for i in range(len2 + 1)] for j in range(len1 + 1)]

    # Then, run recursion.  The following function returns true if we can interleave the last i
    # characters of s1 and the last j characters of s2 to compose the last (i+j) characters of s3
    # (here, i >= 0, j >= 0, and i + j > 0).
    def dfs(i, j):
        if i > len1 or j > len2:
            return False

        if possibleArray[i][j] == 0:
            return False
        if possibleArray[i][j] == 1:
            return True

        if i==0 and j==0:
            possibleArray[i][j] = 1
            return True

        if i > 0 and j == 0:
            if s1[(-i):] == s3[(-i):]:
                possibleArray[i][j] = 1
                return True
            else:
                possibleArray[i][j] = 0
                return False

        if i == 0 and j > 0:
            if s2[(-j):] == s3[(-j):]:
                possibleArray[i][j] = 1
                return True
            else:
                possibleArray[i][j] = 0
                return False

        if (s1[-i] == s3[-(i+j)] and dfs(i-1, j)) or (s2[-j] == s3[-(i+j)] and dfs(i, j-1)):
            possibleArray[i][j] = 1
            return True
        else:
            possibleArray[i][j] = 0
            return False

    return dfs(len1, len2)

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        return checkForInterleaveV2(s1, s2, s3)
