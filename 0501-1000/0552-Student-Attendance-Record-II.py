class Solution(object):
    def checkRecord(self, n):
        def prod(v1, v2):
            return sum([v1[i] * v2[i] for i in range(len(v1))])
        
        def matSum(M1, M2):
            m, n = len(M1), len(M1[0])
            auxMat = [[0] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    auxMat[i][j] = M1[i][j] + M2[i][j]
            
            return auxMat
        
        def matProd(M1, M2):
            M2T = list(map(list, zip(*M2)))
            m, n = len(M1), len(M2T)
            auxMat = [[0] * n for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    auxMat[i][j] = prod(M1[i], M2T[j])
            
            return auxMat
        
        p = 10 ** 9 + 7
        P1 = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        P2 = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        currP = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        currQ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        bits = []
        
        while n > 0:
            bits.append(n % 2)
            n >>= 1
            
        while bits:
            currBit = bits.pop()
            if currBit:
                currQ = matSum(matProd(currQ, P1), matProd(currP, P2))
                currP = matProd(currP, P1)
            if bits:
                currQ = matSum(matProd(currQ, currP), matProd(currP, currQ))
                currP = matProd(currP, currP)
                
        return (currP[0][0] + currP[1][0] + currP[2][0] + currQ[0][0] + currQ[1][0] + currQ[2][0]) % p