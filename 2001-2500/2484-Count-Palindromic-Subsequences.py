class Solution(object):
    def countPalindromes(self, s):
        p = 10 ** 9 + 7
        totalCount = 0
        
        for c1 in range(10):
            for c2 in range(10):
                matchStr = str(c1) + str(c2) + "x" + str(c2) + str(c1)
                partialMatchCount = [0] * 5 + [1]
                
                for i in range(len(s)):
                    for j in range(5):
                        if s[i] == matchStr[j] or j == 2:
                            partialMatchCount[j] += partialMatchCount[j + 1]
                
                totalCount = (totalCount + partialMatchCount[0]) % p
                
        return totalCount