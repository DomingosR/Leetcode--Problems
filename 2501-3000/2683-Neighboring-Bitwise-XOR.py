class Solution(object):
    def doesValidArrayExist(self, derived):
        return reduce(lambda i, j: i ^ j, derived) == 0
