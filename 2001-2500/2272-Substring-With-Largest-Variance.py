class Solution(object):
    def largestVariance(self, s):
        revS = s[::-1]
        letters = set(s)
        pairs = [(s1, s2) for s1 in letters for s2 in letters if s1 != s2]
        maxVar = [0]
        
        def process(s1, s2, inputStr):
            count1 = 0
            count2 = 0

            for letter in inputStr:
                if s1 != letter and s2 != letter:
                    continue
                
                if letter == s1:
                    count1 += 1
                if letter == s2:
                    count2 += 1
                
                if count1 < count2:
                    count1, count2 = 0, 0
                elif count1 > 0 and count2 > 0:
                    maxVar[0] = max(maxVar[0], count1 - count2)
        
        for s1, s2 in pairs:
            process(s1, s2, s)
            process(s1, s2, revS)
        
        return maxVar[0]