class Solution(object):
    def breakPalindrome(self, palindrome):
        n = len(palindrome)
        
        if n == 1:
            return ""

        charsToCheck = n//2

        for i in range(charsToCheck):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]

        return palindrome[:n-1] + "b"
