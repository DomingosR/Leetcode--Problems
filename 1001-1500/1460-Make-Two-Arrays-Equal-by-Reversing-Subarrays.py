class Solution(object):
    def canBeEqual(self, target, arr):
        return Counter(target) == Counter(arr)