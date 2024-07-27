class Solution(object):
    def findTheWinner(self, n, k):
        if k == 1:
            return n
            
        friendNums = list(range(1, n+1))
        i, count = 0, n
        k -= 1
        
        while count > 1:
            i = (i + k) % count
            friendNums.pop(i)
            count -= 1
            i = i % count
            
        return friendNums[0]