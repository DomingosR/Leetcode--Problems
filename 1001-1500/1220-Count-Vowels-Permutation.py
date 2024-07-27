class Solution(object):
    def countVowelPermutation(self, n):
        nA, nE, nI, nO, nU = 1, 1, 1, 1, 1

        for _ in range(n-1):
            nA, nE, nI, nO, nU = nE + nI + nU, nA + nI, nE + nO, nI, nI + nO

        return (nA + nE + nI + nO + nU) % (10**9 + 7)
