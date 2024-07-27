class Solution(object):
    def canBeEqual(self, target, arr):
        return Counter(arr) == Counter(target)