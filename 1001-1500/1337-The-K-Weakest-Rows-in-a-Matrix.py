class Solution(object):
    def kWeakestRows(self, mat, k):
        rowList = [(sum(mat[i]), i) for i in range(len(mat))]
        rowList.sort()
        return [rowList[i][1] for i in range(k)]
