class Solution(object):
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        matT = list(map(list, zip(*mat)))
        numSpecial = 0
        
        for i in range(m):
            if sum(mat[i]) == 1:
                j = mat[i].index(1)
                if sum(matT[j]) == 1:
                    numSpecial += 1
                    
        return numSpecial