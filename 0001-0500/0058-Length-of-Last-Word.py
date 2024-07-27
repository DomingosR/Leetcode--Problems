class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        j = i
        while s[j] != " " and j >= 0:
            j -= 1
        return i - j