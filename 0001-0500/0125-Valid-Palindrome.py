class Solution(object):
    def isPalindrome(self, s):
        adjustedS = ""
        
        for char in s:
            if 65 <= ord(char) <= 90:
                adjustedS += chr(ord(char) + 32)
            if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
                adjustedS += char
        
        return adjustedS == adjustedS[::-1]