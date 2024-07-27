class Solution(object):
    def firstUniqChar(self, s):
        letterCounter = Counter(s)
        
        for i, char in enumerate(s):
            if letterCounter[char] == 1:
                return i
            
        return -1