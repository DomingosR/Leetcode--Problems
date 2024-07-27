class Solution(object):
    def countStudents(self, students, sandwiches):
        n, k = len(students), sum(students)
        numZero, numOne = n-k, k

        for i in range(n):
            if sandwiches[i] == 0:
                if numZero == 0:
                    return n-i
                else:
                    numZero -= 1
            if sandwiches[i] == 1:
                if numOne == 0:
                    return n-i
                else:
                    numOne -= 1
        
        return 0