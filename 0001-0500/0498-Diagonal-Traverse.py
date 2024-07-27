class Solution(object):
    def findDiagonalOrder(self, mat):
        m = len(mat)
        n = len(mat[0])
        diagonals = defaultdict(list)
        returnVal = []

        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])

        for entry in diagonals.items():
            if entry[0] % 2 == 1:
                returnVal.extend([x for x in entry[1]])
            else:
                returnVal.extend([x for x in entry[1][::-1]])

        return returnVal
