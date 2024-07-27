class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        preComputed = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                if s1[i] == s2[j]:
                    preComputed[i+1][j+1] = preComputed[i][j] + ord(s1[i])
                else:
                    preComputed[i+1][j+1] = max(preComputed[i+1][j], preComputed[i][j+1])
        
        return sum(map(ord, s1 + s2)) - 2 * preComputed[n1][n2]