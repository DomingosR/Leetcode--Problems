class Solution(object):
    def minimumLength(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                break
            
            currChar = s[left]
            while s[left] == currChar and left < right:
                left += 1
            while s[right] == currChar and left < right:
                right -= 1
            
            if left == right and s[left] == currChar:
                return 0
        
        return right - left + 1