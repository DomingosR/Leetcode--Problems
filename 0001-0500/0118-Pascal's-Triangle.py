def findTriangle(n):
    if n == 1:
        return [[1]] 
    
    if n == 2:
        return [[1], [1, 1]] 
    
    i = 2
    answer = [[1], [1, 1]] 
    
    while i < n:
        list1 = [0] + answer[-1]    
        list2 = answer[-1] + [0]
        list3 = [sum(tup) for tup in zip(list1, list2)]
        answer.append(list3)
        i += 1
    
    return answer

class Solution(object):
    def generate(self, numRows):
        return findTriangle(numRows)