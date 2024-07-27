class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        editDistance = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            editDistance[i][0] = i

        for j in range(n+1):
            editDistance[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    editDistance[i][j] = editDistance[i-1][j-1]
                else:
                    insert = 1 + editDistance[i-1][j]
                    delete = 1 + editDistance[i][j-1]
                    replace = 1 + editDistance[i-1][j-1]
                    editDistance[i][j] = min(insert, delete, replace)

        return editDistance[-1][-1]
