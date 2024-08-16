class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        m, n = len(students), len(students[0])
        compatibility = [[0] * m for _ in range(m)]
        maxScore = 0
        
        for i in range(m):
            for j in range(m):
                compatibility[i][j] = sum([1 for k in range(n) if students[i][k] == mentors[j][k]])
                
        for indPerm in permutations(range(m)):
            maxScore = max(maxScore, sum([compatibility[i][indPerm[i]] for i in range(m)]))
            
        return maxScore