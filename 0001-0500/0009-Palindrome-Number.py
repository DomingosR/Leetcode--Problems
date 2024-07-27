class Solution(object):
    def isPalindrome(self, x):
        strX = str(x)
        return strX == strX[::-1]