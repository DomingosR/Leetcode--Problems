class Solution(object):
    def reorganizeString(self, s):
        if len(s) == 1: return s
        s = sorted(sorted(s), key = s.count, reverse = True)
        s[::2], s[1::2] = s[:(len(s)+1)//2], s[(len(s)+1)//2:]
        return '' if s[0] == s[1] else ''.join(s)