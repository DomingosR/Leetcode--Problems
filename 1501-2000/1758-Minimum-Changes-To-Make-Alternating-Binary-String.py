class Solution(object):
    def minOperations(self, s):
        digitCount = [0, 0]
        
        for i in range(len(s)):
            digitCount[(i + int(s[i])) % 2] += 1
            
        return min(digitCount)