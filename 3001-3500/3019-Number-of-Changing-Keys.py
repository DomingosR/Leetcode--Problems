class Solution(object):
    def countKeyChanges(self, s):
        return len([i for i in range(len(s) - 1) if s[i].lower() != s[i + 1].lower()])
