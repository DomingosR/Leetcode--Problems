class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        numSubmatrices = 0

        prefixSum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefixSum[i][j] = matrix[i][j] + (prefixSum[i][j-1] if j > 0 else 0)

        for j1 in range(n):
            for j2 in range(j1, n):
                auxSums = {0: 1}
                s = 0
                for i in range(m):
                    s += prefixSum[i][j2] - (prefixSum[i][j1-1] if j1 > 0 else 0)
                    numSubmatrices += auxSums.get(s - target, 0)
                    auxSums[s] = auxSums.get(s, 0) + 1

        return numSubmatrices 
