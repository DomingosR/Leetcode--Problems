class Solution(object):
    def canReach(self, s, minJump, maxJump):
        reachable = [char == "0" for char in s]
        slidingSum = 0

        for i in range(1, len(s)):
            if i >= minJump: 
                slidingSum += reachable[i - minJump]
            if i > maxJump: 
                slidingSum -= reachable[i - maxJump - 1]
            reachable[i] &= (slidingSum > 0)

        return reachable[-1]